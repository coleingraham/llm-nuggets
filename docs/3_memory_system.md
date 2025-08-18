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
 AIMessage(content="I don't have access to your personal preferences or data, so I can't know your favorite animal. However, I'd love to learn more about animals and can help you explore different species, their habitats, behaviors, or even help you choose a favorite based on your interests! What kind of animals do you like? 🐾", additional_kwargs={}, response_metadata={}),
 HumanMessage(content='I love cats!', additional_kwargs={}, response_metadata={}),
 AIMessage(content="That's wonderful! 🐱 Cats are amazing creatures—they're independent, curious, and have a way of making everyone smile. Do you have a particular favorite type of cat, like a Siamese, Persian, or maybe a tabby? Or do you prefer the wild ones, like tigers or leopards? I'd love to hear more about what you enjoy about cats!", additional_kwargs={}, response_metadata={})]
Memories:
['The user loves cats.']

Second conversation:
[SystemMessage(content='Do not say "based on your previous messages"\nHere are your previous memories:\n["The user loves cats."]', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='what is my favorite animal?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Based on your previous message, it seems like your favorite animal is a cat! 🐱 Do you love cats?', additional_kwargs={}, response_metadata={})]
Memories:
['The user loves cats.', "The user's favorite animal is a cat."]
```
