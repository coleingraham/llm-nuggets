# Filtering Chat History

One of the challenges with LLMs is dealing with long contexts. As the
length of the chat history increases, the cost of each request increases,
and you run into the [lost in the middle](https://arxiv.org/abs/2307.03172)
problem, degrading performance. A simple technique for managing this is to
just send the previous few messages as context in a long chat. This obviously
has limitations, so in practice it should be paired with other techniques,
but it's fairly straightforward to implement.

# Example Usage

```
$ cd src
$ python filtered_history.py --provider ollama --model qwen3:8b --temperature 0.3

Full History
============
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='hi!', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Hello! How can I assist you today? 😊', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='how are you?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="I'm just a virtual assistant, so I don't have feelings, but I'm here and ready to help you! How are you doing? 😊", additional_kwargs={}, response_metadata={}),
 HumanMessage(content="I'm fine too.", additional_kwargs={}, response_metadata={}),
 AIMessage(content="That's great to hear! 😊 If you need help with anything, just let me know. Have a wonderful day!", additional_kwargs={}, response_metadata={}),
 HumanMessage(content='how can I square a circle?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Squaring a circle is a classic geometric problem that has intrigued mathematicians for centuries. The goal is to construct a square with the **same area** as a given circle, using only a **compass and straightedge** (i.e., classical geometric constructions). \n\nHowever, this problem was **proven to be impossible** in 1882 by the German mathematician **Ferdinand von Lindemann**, who showed that **π (pi)** is a **transcendental number**. This means it cannot be the root of any non-zero polynomial equation with rational coefficients. Because of this, it\'s **impossible to construct a square with the same area as a given circle using only a compass and straightedge**.\n\n### But here\'s the good news:\nIf you\'re not restricted to classical geometric constructions, you can "square a circle" in a few different ways:\n\n---\n\n### 1. **Mathematically (using area):**\nIf you have a circle with radius $ r $, its area is:\n$$\nA = \\pi r^2\n$$\nTo find the side length $ s $ of a square with the same area:\n$$\ns = \\sqrt{\\pi r^2} = r \\sqrt{\\pi}\n$$\nSo, the square has side length $ r \\sqrt{\\pi} $.\n\n---\n\n### 2. **Using approximation:**\nYou can approximate the square by using a value for π (like 3.1416) and then calculating the side length of the square. For example, if the radius of the circle is 1, the area is about 3.1416, and the square would have a side length of about 1.77245.\n\n---\n\n### 3. **Using technology:**\nIf you\'re using a computer or drawing software, you can easily create a square with the same area as a circle by calculating the side length and drawing it.\n\n---\n\nSo, while you can\'t do it with just a compass and straightedge, you can do it **mathematically** or with **modern tools**. Let me know if you\'d like help calculating it for a specific circle! 😊', additional_kwargs={}, response_metadata={})]

Filtered History
================
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='how can I square a circle?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Squaring a circle is a classic geometric problem that has intrigued mathematicians for centuries. The goal is to construct a square with the **same area** as a given circle, using only a **compass and straightedge** (i.e., classical geometric constructions). \n\nHowever, this problem was **proven to be impossible** in 1882 by the German mathematician **Ferdinand von Lindemann**, who showed that **π (pi)** is a **transcendental number**. This means it cannot be the root of any non-zero polynomial equation with rational coefficients. Because of this, it\'s **impossible to construct a square with the same area as a given circle using only a compass and straightedge**.\n\n### But here\'s the good news:\nIf you\'re not restricted to classical geometric constructions, you can "square a circle" in a few different ways:\n\n---\n\n### 1. **Mathematically (using area):**\nIf you have a circle with radius $ r $, its area is:\n$$\nA = \\pi r^2\n$$\nTo find the side length $ s $ of a square with the same area:\n$$\ns = \\sqrt{\\pi r^2} = r \\sqrt{\\pi}\n$$\nSo, the square has side length $ r \\sqrt{\\pi} $.\n\n---\n\n### 2. **Using approximation:**\nYou can approximate the square by using a value for π (like 3.1416) and then calculating the side length of the square. For example, if the radius of the circle is 1, the area is about 3.1416, and the square would have a side length of about 1.77245.\n\n---\n\n### 3. **Using technology:**\nIf you\'re using a computer or drawing software, you can easily create a square with the same area as a circle by calculating the side length and drawing it.\n\n---\n\nSo, while you can\'t do it with just a compass and straightedge, you can do it **mathematically** or with **modern tools**. Let me know if you\'d like help calculating it for a specific circle! 😊', additional_kwargs={}, response_metadata={})]

total token usage: {'qwen3:8b': {'input_tokens': 325, 'output_tokens': 523, 'total_tokens': 848}}
```
