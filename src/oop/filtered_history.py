from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


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
                 should_filter=False,
                 max_history=2):
        self.llm = llm
        self.max_history = max_history
        self.should_filter = should_filter
        if messages is None:
            messages = []
        self.messages = messages

        if system_prompt is None:
            system_prompt = 'You are a helpful assistant.'
        self.system_prompt = system_prompt

    def get_messages(self, should_filter=False):
        messages = self.messages
        if should_filter:
            messages = messages[-self.max_history:]
        return [SystemMessage(self.system_prompt)] + messages

    def chat(self, prompt):
        """Maintain the message history and handle calling the llm."""
        self.messages.append(HumanMessage(prompt))
        response = self.llm.invoke(self.get_messages(self.should_filter))
        content = response.content
        self.messages.append(AIMessage(content))
        return content


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback
    with get_usage_metadata_callback() as cb:
        chatbot = Chatbot(llm)
        chatbot.chat('hi!')
        chatbot.chat('how are you?')
        chatbot.chat("I'm fine too.")
        chatbot.chat('how can I square a circle?')
        print('Full History')
        print('============')
        pprint(chatbot.get_messages())
        print('\nFiltered History')
        print('================')
        pprint(chatbot.get_messages(True))
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
