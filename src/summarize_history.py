from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


class History:
    def __init__(self,
                 llm,
                 max_history=2):
        self.llm = llm
        self.max_history = max_history
        self.previous = []
        self.current = []
        self.summary = ''

    def summarize(self, new_messages):
        messages = [
                HumanMessage(f'''Here is a summary of a conversation so far:

"{self.summary}"

Here is what has been said since then:

"{new_messages}"

Provide an updated summary of the key information from the conversation.
Only include the most important information from both the existing summary
and the new conversation. Provide only the new summary with no additional text.
''')]
        response = self.llm.invoke(messages)
        self.summary = response.content

    def update(self, new_messages: list[str]):
        # TODO: change this to buffer max_history messages rather than always update
        self.current.extend(new_messages)
        to_summarize = self.current[:-self.max_history]
        self.current = self.current[-self.max_history:]
        self.summarize(' '.join([x.content for x in to_summarize]))
        self.previous.extend(to_summarize)

    def get_messages(self):
        messages = [HumanMessage(f'''Here is a summary of the previous
conversation:

"{self.summary}"
''')]
        messages.extend(self.current)

        return messages

    def get_full_history(self):
        return self.previous + self.current


class Chatbot:
    """Basic conversational chatbot that maintains the conversation history.

    Args:
        llm: an instance of a langchain model of your choice
        system_prompt: the text to a system prompt to use, if any
        messages: a list of previous messages, if any
        max_history: the number of recent messages to keep in the context
    """
    def __init__(self,
                 llm,
                 system_prompt=None,
                 messages=None,
                 max_history=2):
        self.llm = llm
        if messages is None:
            messages = []
        self.history = History(llm, max_history)

        if system_prompt is None:
            system_prompt = 'You are a helpful assistant.'
        self.system_prompt = system_prompt

    def get_messages(self):
        messages = self.history.get_messages()
        return [SystemMessage(self.system_prompt)] + messages

    def get_full_history(self):
        messages = self.history.get_full_history()
        return [SystemMessage(self.system_prompt)] + messages

    def chat(self, prompt):
        """Maintain the message history and handle calling the llm."""
        messages = self.get_messages()
        messages.append(HumanMessage(prompt))
        response = self.llm.invoke(messages)
        content = response.content
        self.history.update([HumanMessage(prompt), AIMessage(content)])
        return content


def test_history(llm):
    from pprint import pprint
    hist = History(llm)

    # deal with an initial history
    hist.update([
        HumanMessage('hi'),
        AIMessage('Hello! How can I assist you?'),
        HumanMessage('I want to buy a boat.'),
        AIMessage('''Are you sure? Boats have a reputation for being a hole in
the water that you pour money into'''),
        HumanMessage('yes I am sure.'),
        AIMessage('If you insist. What kind of boat are you thinking of?'),
        HumanMessage('a speed boat.'),
        AIMessage('Then you had better act fast!'),
        ])

    # add to it
    hist.update([
        HumanMessage('how much will that cost?'),
        AIMessage('A metric boat load!'),
        ])

    print('Summary')
    print('=======')
    print(hist.summary)
    print('\nPrevious')
    print('========')
    pprint(hist.previous)
    print('\nCurrent')
    print('=======')
    pprint(hist.current)


def test(llm):
    from pprint import pprint
    chatbot = Chatbot(llm)
    chatbot.chat('hi!')
    chatbot.chat('how are you?')
    chatbot.chat("I'm fine too.")
    chatbot.chat('how can I square a circle?')
    chatbot.chat('can you give me an example?')
    print('Full History')
    print('============')
    pprint(chatbot.get_full_history())
    print('\nFiltered History')
    print('================')
    pprint(chatbot.get_messages())


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
