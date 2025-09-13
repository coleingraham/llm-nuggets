from typing import List, Optional

from langchain_core.messages import (
        AIMessage,
        BaseMessage,
        HumanMessage,
        SystemMessage)
from pydantic import BaseModel


class History(BaseModel):
    system_prompt: Optional[SystemMessage] = None
    messages: List[BaseMessage] = []
    max_history: int = 2

    def append(self, message):
        self.messages.append(message)

    def get_messages(self, should_filter=False):
        messages = self.messages
        if should_filter:
            messages = messages[-self.max_history:]
        if self.system_prompt is not None:
            return [self.system_prompt] + messages
        else:
            return messages


def chat(llm,
         history: History,
         prompt: str,
         should_filter: bool = True) -> History:
    """Maintain the message history and handle calling the llm."""
    history = history.model_copy()
    history.append(HumanMessage(prompt))
    response = llm.invoke(history.get_messages(should_filter))
    content = response.content
    history.append(AIMessage(content))
    return history


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback

    history = History(
            system_prompt=SystemMessage('you are a helpful assistant'))

    with get_usage_metadata_callback() as cb:
        history = chat(llm, history, 'hi!')
        history = chat(llm, history, 'how are you?')
        history = chat(llm, history, "I'm fine too.")
        history = chat(llm, history, 'how can I square a circle?')
        print('Full History')
        print('============')
        pprint(history.get_messages())
        print('\nFiltered History')
        print('================')
        pprint(history.get_messages(True))
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
