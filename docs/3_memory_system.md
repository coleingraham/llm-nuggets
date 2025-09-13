# Simplistic ChatGPT Style Memory System Clone

If you have used the web interface for [ChatGPT](https://chatgpt.com/) you
may have seen the "memory updated" message pop up when you say something about
yourself. This can be managed through your personalization settings, but here
I want to provide an example implementation for handling the actual memory
extraction part of the system.

# Example Usage

```
$ cd src
$ python memory_system.py --provider ollama --model qwen3:8b --temperature 0.3

Original conversation:
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='what is my favorite animal?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="I don't have access to your personal preferences or data about your favorite animal. However, I can help you explore different animals and their characteristics if you'd like! What kind of animals interest you?", additional_kwargs={}, response_metadata={}),
 HumanMessage(content='I love cats!', additional_kwargs={}, response_metadata={}),
 AIMessage(content="That's wonderful! Cats are amazing creatures — curious, independent, and full of personality. They make great companions and have a way of bringing joy into our lives. Do you have a particular favorite type of cat, like a Siamese, Persian, or maybe a tabby? Or is there something specific about cats that you love? I'd love to hear more! 🐾", additional_kwargs={}, response_metadata={})]
Memories:
['The user loves cats']

memory system token usage: {'qwen3:8b': {'total_tokens': 303, 'output_tokens': 29, 'input_tokens': 274}}
chat token usage: {'qwen3:8b': {'total_tokens': 240, 'output_tokens': 120, 'input_tokens': 120}}

Second conversation:
[SystemMessage(content='Do not say "based on your previous messages"\nHere are your previous memories:\n["The user loves cats"]', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='what is my favorite animal?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Based on your previous message, it seems like your favorite animal is a cat! 🐱 Do you love cats?', additional_kwargs={}, response_metadata={})]
Memories:
['The user loves cats', "The user's favorite animal is a cat"]

memory system token usage: {'qwen3:8b': {'input_tokens': 142, 'output_tokens': 21, 'total_tokens': 163}}
chat token usage: {'qwen3:8b': {'input_tokens': 49, 'output_tokens': 25, 'total_tokens': 74}}

total token usage: {'qwen3:8b': {'total_tokens': 780, 'output_tokens': 195, 'input_tokens': 585}}
```
