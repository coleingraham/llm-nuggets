from typing import List, Optional

from langchain_core.messages import (
        AIMessage,
        BaseMessage,
        HumanMessage,
        SystemMessage)


def get_messages(messages: List[BaseMessage] = [],
                 system_prompt: Optional[SystemMessage] = None,
                 max_history: int = 2,
                 should_filter: bool = False,
                 **kwargs) -> List[BaseMessage]:
    if should_filter:
        messages = messages[-max_history:]
    if system_prompt is not None:
        return [system_prompt] + messages
    else:
        return messages


def chat(prompt: str,
         llm,
         messages: List[BaseMessage],
         **kwargs) -> List[BaseMessage]:
    messages = messages.copy()
    messages.append(HumanMessage(prompt))
    response = llm.invoke(get_messages(messages, **kwargs))
    messages.append(AIMessage(response.content))
    return messages


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback

    state = {
            'llm': llm,
            'system_prompt': SystemMessage('you are a helpful assistant'),
            'max_history': 2,
            'should_filter': True,
            'messages': []
            }

    with get_usage_metadata_callback() as cb:
        state['messages'] = chat('hi!', **state)
        state['messages'] = chat('how are you?', **state)
        state['messages'] = chat("I'm fine too.", **state)
        state['messages'] = chat('how can I square a circle?', **state)

        print('Full History')
        print('============')
        pprint(get_messages(messages=state['messages'],
                            system_prompt=state['system_prompt']))
        print('\nFiltered History')
        print('================')
        pprint(get_messages(**state))

    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
