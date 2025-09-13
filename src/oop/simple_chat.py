from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


class Chatbot:
    """Basic conversational chatbot that maintains the conversation history.

    Args:
        llm: an instance of a langchain model of your choice
        system_prompt: the text to a system prompt to use, if any
        messages: a list of previous messages, if any
    """
    def __init__(self, llm, system_prompt=None, messages=None):
        self.llm = llm
        if messages is None:
            messages = []
        self.messages = messages
        # only apply the system prompt if we do not have a message history
        if system_prompt and len(self.messages) > 0:
            self.messages.append(SystemMessage(system_prompt))

    def chat(self, prompt):
        """Maintain the message history and handle calling the llm."""
        self.messages.append(HumanMessage(prompt))
        response = self.llm.invoke(self.messages)
        content = response.content
        self.messages.append(AIMessage(content))
        return content


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback
    with get_usage_metadata_callback() as cb:
        chatbot = Chatbot(llm, 'you are very funny')
        chatbot.chat('tell me a joke')
        chatbot.chat('tell me another')
        pprint(chatbot.messages)
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
