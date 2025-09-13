import json
from typing import List, Optional

from langchain_core.callbacks import UsageMetadataCallbackHandler
from langchain_core.messages import (
        AIMessage,
        BaseMessage,
        HumanMessage,
        SystemMessage)

from utils import get_json_from_response


def extract_memories(prompt: str,
                     memory_llm,
                     memories: List[str],
                     memory_usage_callback=None,
                     **kwargs) -> List[BaseMessage]:
    messages = [
            SystemMessage(f'''your job is to identify things worth remembering.
you will be given some text and you should respond in the following JSON
format:

```json
{{
    "memory": <a list of individual new facts worth remembering, empty if none>
}}
```

here are the existing memories:
{json.dumps(memories)}

if a memory already exists, or if it was referenced earlier in the
conversation, do not include it in the list. only include new information.
if there is no new information, return an empty list.
only output the JSON object in a markdown block.
'''),
            HumanMessage(prompt)
        ]

    completion = memory_llm.invoke(messages,
                                   config={"callbacks":
                                           [memory_usage_callback]})

    response = get_json_from_response(completion.content)
    new_memories = memories.copy()
    new_memories.extend(response['memory'])
    return new_memories


def get_response(prompt: str,
                 llm,
                 messages: List[BaseMessage],
                 chatbot_usage_callback=None,
                 **kwargs) -> List[BaseMessage]:
    messages = messages.copy()
    messages.append(HumanMessage(prompt))
    response = llm.invoke(messages,
                          config={"callbacks":
                                  [chatbot_usage_callback]})
    messages.append(AIMessage(response.content))
    return messages


def chat(prompt: str,
         state: dict) -> dict:
    new_state = state.copy()
    new_state['memories'] = extract_memories(prompt, **state)
    new_state['messages'] = get_response(prompt, **state)
    return new_state


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback

    with get_usage_metadata_callback() as cb:
        state = {'llm': llm,
                 'memory_llm': llm,
                 'chatbot_usage_callback': UsageMetadataCallbackHandler(),
                 'memory_usage_callback': UsageMetadataCallbackHandler(),
                 'messages': [],
                 'memories': []}

        state = chat('what is my favorite animal?', state)
        state = chat('I love cats!', state)
        print('Original conversation:')
        pprint(state['messages'])
        print('Memories:')
        pprint(state['memories'])
        print('\nmemory system token usage:',
              state['memory_usage_callback'].usage_metadata)
        print('chat token usage:',
              state['chatbot_usage_callback'].usage_metadata)

        new_state = {'llm': llm,
                     'memory_llm': llm,
                     'chatbot_usage_callback': UsageMetadataCallbackHandler(),
                     'memory_usage_callback': UsageMetadataCallbackHandler(),
                     'messages': [SystemMessage(f'''
Do not say things like "based on your previous messages" in your responses.
Here are your previous memories:
{json.dumps(state['memories'])}''')],
                     'memories': state['memories']}

        new_state = chat('what is my favorite animal?', new_state)
        print('\nSecond conversation:')
        pprint(new_state['messages'])
        print('Memories:')
        pprint(new_state['memories'])
        print('\nmemory system token usage:',
              new_state['memory_usage_callback'].usage_metadata)
        print('chat token usage:',
              new_state['chatbot_usage_callback'].usage_metadata)

    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
