# Chat History Summarization

Building on top of the [filtered history example](2_filtered_history.md),
we generally need something more than just omitting previous messages. One
extension to this is to create a summary of the important information in the
chat history, and then provide that along with the most recent messages.

# Example Usage

```
$ cd src
$ python summarize_history.py --provider ollama --model qwen3:8b --temperature 0.3

Full History
============
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='hi!', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Hello! How can I assist you today? 😊', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='how are you?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="I'm just a virtual assistant, so I don't have feelings, but I'm here and ready to help you! How can I assist you today? 😊", additional_kwargs={}, response_metadata={}),
 HumanMessage(content="I'm fine too.", additional_kwargs={}, response_metadata={}),
 AIMessage(content="That's great to hear! 😊 If you need any help or have any questions, feel free to ask. Have a wonderful day!", additional_kwargs={}, response_metadata={}),
 HumanMessage(content='how can I square a circle?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="Squaring a circle is a classic geometric problem that has intrigued mathematicians for centuries. The goal is to construct a square with the same area as a given circle using only a compass and straightedge. However, this task is mathematically impossible under the traditional rules of classical geometry.\n\n### Why is it impossible?\nThe problem was proven to be impossible in 1882 by the German mathematician **Ferdinand von Lindemann**, who showed that **π (pi)** is a **transcendental number**. This means that π cannot be the root of any non-zero polynomial equation with rational coefficients. Since constructing a square with the same area as a circle would require solving such an equation, it's fundamentally impossible with compass and straightedge alone.\n\n### What does this mean for practical purposes?\n- **In theory**: Squaring the circle is impossible under classical geometric constraints.\n- **In practice**: You can approximate it using modern tools or numerical methods. For example:\n  - Calculate the area of the circle: $ A = \\pi r^2 $\n  - Find the side length of the square: $ s = \\sqrt{A} = \\sqrt{\\pi r^2} = r \\sqrt{\\pi} $\n  - Use this side length to construct a square with approximately the same area as the circle.\n\n### Summary\n- **Impossible with compass and straightedge** (classical geometry).\n- **Possible with modern tools or approximations**.\n\nLet me know if you'd like help calculating the side length of a square with the same area as a given circle! 📐📐", additional_kwargs={}, response_metadata={}),
 HumanMessage(content='can you give me an example?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Sure! Let\'s walk through an example step by step.\n\n### Example:\nSuppose you have a **circle with a radius of 2 units**.\n\n---\n\n### Step 1: Calculate the area of the circle\n$$\n\\text{Area of the circle} = \\pi r^2 = \\pi \\times 2^2 = 4\\pi \\text{ square units}\n$$\n\n---\n\n### Step 2: Find the side length of the square with the same area\n$$\n\\text{Area of the square} = s^2 = 4\\pi\n$$\n$$\ns = \\sqrt{4\\pi} = 2\\sqrt{\\pi} \\approx 2 \\times 1.772 = 3.544 \\text{ units}\n$$\n\n---\n\n### Step 3: Construct the square\nUsing a ruler and compass, you can construct a square with side length approximately **3.544 units**. This square will have an area very close to that of the original circle.\n\n---\n\n### Final Result:\n- **Circle radius**: 2 units  \n- **Circle area**: $ 4\\pi \\approx 12.566 $ square units  \n- **Square side length**: $ \\approx 3.544 $ units  \n- **Square area**: $ \\approx 12.566 $ square units (same as the circle)\n\n---\n\n### Note:\nWhile this is an **approximation**, it shows how you can "square a circle" in practice using modern tools or numerical methods. If you\'d like, I can help you calculate this for any radius you choose! 📐📏', additional_kwargs={}, response_metadata={})]

Filtered History
================
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='Here is a summary of the previous\nconversation:\n\n"Squaring a circle is mathematically impossible using only a compass and straightedge because π is a transcendental number, proven by Ferdinand von Lindemann in 1882. However, it can be approximated with modern tools or numerical methods by calculating the square\'s side length as $ r \\sqrt{\\pi} $, where $ r $ is the circle\'s radius."\n', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='can you give me an example?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='Sure! Let\'s walk through an example step by step.\n\n### Example:\nSuppose you have a **circle with a radius of 2 units**.\n\n---\n\n### Step 1: Calculate the area of the circle\n$$\n\\text{Area of the circle} = \\pi r^2 = \\pi \\times 2^2 = 4\\pi \\text{ square units}\n$$\n\n---\n\n### Step 2: Find the side length of the square with the same area\n$$\n\\text{Area of the square} = s^2 = 4\\pi\n$$\n$$\ns = \\sqrt{4\\pi} = 2\\sqrt{\\pi} \\approx 2 \\times 1.772 = 3.544 \\text{ units}\n$$\n\n---\n\n### Step 3: Construct the square\nUsing a ruler and compass, you can construct a square with side length approximately **3.544 units**. This square will have an area very close to that of the original circle.\n\n---\n\n### Final Result:\n- **Circle radius**: 2 units  \n- **Circle area**: $ 4\\pi \\approx 12.566 $ square units  \n- **Square side length**: $ \\approx 3.544 $ units  \n- **Square area**: $ \\approx 12.566 $ square units (same as the circle)\n\n---\n\n### Note:\nWhile this is an **approximation**, it shows how you can "square a circle" in practice using modern tools or numerical methods. If you\'d like, I can help you calculate this for any radius you choose! 📐📏', additional_kwargs={}, response_metadata={})]
```
