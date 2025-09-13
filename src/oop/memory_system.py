import json
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.callbacks import UsageMetadataCallbackHandler

from utils import get_json_from_response


class MemoryExtractor:
    def __init__(self, llm, memories):
        self.llm = llm
        self.memories = memories
        self.usage_callback = UsageMetadataCallbackHandler()

    def extract_memories(self, prompt):
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
{json.dumps(self.memories)}

if a memory already exists, or if it was referenced earlier in the
conversation, do not include it in the list. only include new information.
if there is no new information, return an empty list.
only output the JSON object in a markdown block.
'''),
            HumanMessage(prompt)
        ]

        completion = self.llm.invoke(messages,
                                     config={"callbacks":
                                             [self.usage_callback]})

        response = get_json_from_response(completion.content)
        # store memories for later
        self.memories.extend(response['memory'])

    def usage_metadata(self):
        return self.usage_callback.usage_metadata


class Chatbot:
    """Basic conversational chatbot that maintains the conversation history.

    Args:
        llm: an instance of a langchain model of your choice
        system_prompt: the text to a system prompt to use, if any
        messages: a list of previous messages, if any
        memories: a list of previous memories, if any
        max_history: the number of recent messages to keep in the context
    """
    def __init__(self,
                 llm,
                 system_prompt=None,
                 messages=None,
                 memories=None,
                 should_filter=False,
                 max_history=2):
        self.llm = llm
        self.usage_callback = UsageMetadataCallbackHandler()
        self.max_history = max_history
        self.should_filter = should_filter
        if messages is None:
            messages = []
        self.messages = messages

        if system_prompt is None:
            system_prompt = 'You are a helpful assistant.'
        self.system_prompt = system_prompt

        if memories is None:
            memories = []
        else:
            self.system_prompt += f'''\nHere are your previous memories:
{json.dumps(memories)}'''

        self.memory_extractor = MemoryExtractor(llm, memories)

    def get_messages(self, should_filter=False):
        messages = self.messages
        if should_filter:
            messages = messages[-self.max_history:]
        return [SystemMessage(self.system_prompt)] + messages

    def get_memories(self):
        return self.memory_extractor.memories

    def chat(self, prompt):
        """Maintain the message history and handle calling the llm."""
        self.memory_extractor.extract_memories(prompt)
        self.messages.append(HumanMessage(prompt))
        response = self.llm.invoke(self.get_messages(self.should_filter),
                                   config={'callbacks': [self.usage_callback]})
        content = response.content
        self.messages.append(AIMessage(content))
        return content

    def usage_metadata(self):
        return self.usage_callback.usage_metadata


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback
    with get_usage_metadata_callback() as cb:
        chatbot = Chatbot(llm)
        chatbot.chat('what is my favorite animal?')
        chatbot.chat('I love cats!')
        print('Original conversation:')
        pprint(chatbot.get_messages())
        print('Memories:')
        memories = chatbot.get_memories()
        print(memories)
        print('\nmemory system token usage:',
              chatbot.memory_extractor.usage_metadata())
        print('chat token usage:', chatbot.usage_metadata())

        chatbot = Chatbot(llm,
                          'Do not say "based on your previous messages"',
                          memories=memories)
        chatbot.chat('what is my favorite animal?')
        print('\nSecond conversation:')
        pprint(chatbot.get_messages())
        print('Memories:')
        memories = chatbot.get_memories()
        print(memories)
        print('\nmemory system token usage:',
              chatbot.memory_extractor.usage_metadata())
        print('chat token usage:', chatbot.usage_metadata())
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
