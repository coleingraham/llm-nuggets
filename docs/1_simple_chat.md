# Basic Chat Wrapper

This is meant to demonstrate how you are intended to manage the message
history of a chat in the style of web interfaces like ChatGPT. Basically
it keeps a history of messages, appends new user messages when sent, and
appends the AI response to the history before returning it to the caller.

# Example Usage

```
$ cd src
$ python -m oop.simple_chat --provider ollama --model qwen3:8b --temperature 0.3

[HumanMessage(content='tell me a joke', additional_kwargs={}, response_metadata={}),
 AIMessage(content="Sure! Here's a joke for you:\n\nWhy don't skeletons fight each other?  \nBecause they don't have the *guts*! 😄", additional_kwargs={}, response_metadata={}),
 HumanMessage(content='tell me another', additional_kwargs={}, response_metadata={}),
 AIMessage(content="Of course! Here's another one:\n\nWhy did the scarecrow win an award?  \nBecause he was outstanding in his field! 🌾😄", additional_kwargs={}, response_metadata={})]

total token usage: {'qwen3:8b': {'output_tokens': 63, 'total_tokens': 147, 'input_tokens': 84}}
```
