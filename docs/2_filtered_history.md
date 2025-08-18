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
 AIMessage(content="I'm just a virtual assistant, so I don't have feelings, but I'm here and ready to help you! How are you doing today? 😊", additional_kwargs={}, response_metadata={}),
 HumanMessage(content="I'm fine too.", additional_kwargs={}, response_metadata={}),
 AIMessage(content="That's great to hear! 😊 If you need help with anything, just let me know. Have a wonderful day!", additional_kwargs={}, response_metadata={}),
 HumanMessage(content='how can I square a circle?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="Squaring a circle is a classic geometric problem that has intrigued mathematicians for centuries. The goal is to construct a square with the **same area** as a given circle, using only a **compass and straightedge** (i.e., classical geometric construction).\n\nHowever, here's the catch:\n\n### 🚫 **It's impossible** to square a circle using only a compass and straightedge.\n\n### Why?\nIn 1882, the German mathematician **Ferdinand von Lindemann** proved that **π (pi)** is a **transcendental number**. This means that π cannot be the root of any non-zero polynomial equation with rational coefficients. As a result, it's **impossible to construct a square with the same area as a given circle using only a compass and straightedge**.\n\n---\n\n### 🔄 But here's the good news:\nYou **can** square a circle in a more practical or mathematical sense — for example:\n\n1. **Using calculus or algebra**:\n   - If you have a circle with radius $ r $, its area is $ A = \\pi r^2 $.\n   - To find the side length $ s $ of a square with the same area:\n     $$\n     s = \\sqrt{\\pi r^2} = r \\sqrt{\\pi}\n     $$\n   - So, the square has side length $ r \\sqrt{\\pi} $.\n\n2. **Using a computer or advanced tools**:\n   - You can approximate the square using numerical methods or software.\n\n---\n\n### 🧠 Summary:\n- **Classical geometry (compass and straightedge)**: **Impossible**.\n- **Modern math or approximation**: **Possible**.\n\nLet me know if you'd like help calculating it for a specific circle! 😊", additional_kwargs={}, response_metadata={})]

Filtered History
================
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='how can I square a circle?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="Squaring a circle is a classic geometric problem that has intrigued mathematicians for centuries. The goal is to construct a square with the **same area** as a given circle, using only a **compass and straightedge** (i.e., classical geometric construction).\n\nHowever, here's the catch:\n\n### 🚫 **It's impossible** to square a circle using only a compass and straightedge.\n\n### Why?\nIn 1882, the German mathematician **Ferdinand von Lindemann** proved that **π (pi)** is a **transcendental number**. This means that π cannot be the root of any non-zero polynomial equation with rational coefficients. As a result, it's **impossible to construct a square with the same area as a given circle using only a compass and straightedge**.\n\n---\n\n### 🔄 But here's the good news:\nYou **can** square a circle in a more practical or mathematical sense — for example:\n\n1. **Using calculus or algebra**:\n   - If you have a circle with radius $ r $, its area is $ A = \\pi r^2 $.\n   - To find the side length $ s $ of a square with the same area:\n     $$\n     s = \\sqrt{\\pi r^2} = r \\sqrt{\\pi}\n     $$\n   - So, the square has side length $ r \\sqrt{\\pi} $.\n\n2. **Using a computer or advanced tools**:\n   - You can approximate the square using numerical methods or software.\n\n---\n\n### 🧠 Summary:\n- **Classical geometry (compass and straightedge)**: **Impossible**.\n- **Modern math or approximation**: **Possible**.\n\nLet me know if you'd like help calculating it for a specific circle! 😊", additional_kwargs={}, response_metadata={})]
```
