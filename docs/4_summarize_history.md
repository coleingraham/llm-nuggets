# Chat History Summarization

Building on top of the [filtered history example](2_filtered_history.md),
we generally need something more than just omitting previous messages. One
extension to this is to create a summary of the important information in the
chat history, and then provide that along with the most recent messages.

# Example Usage

```
$ cd src
$ python -m oop.summarize_history --provider ollama --model qwen3:8b --temperature 0.3

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
 AIMessage(content='Squaring a circle is a classic geometric problem that has been a subject of fascination and mathematical inquiry for centuries. The goal of the problem is to construct a square with the same area as a given circle, using only a compass and straightedge. However, this task is mathematically impossible under the classical constraints of Euclidean geometry.\n\n### Why is it impossible?\nThe problem was proven to be impossible in 1882 by the German mathematician **Ferdinand von Lindemann**, who showed that **π (pi)** is a **transcendental number**. A transcendental number is not a root of any non-zero polynomial equation with rational coefficients. This means that it is impossible to construct a square with the same area as a given circle using only a compass and straightedge, because such a construction would require the exact value of π, which cannot be achieved through these classical tools.\n\n### What does this mean for practical purposes?\nWhile it is impossible to "square a circle" in the classical geometric sense, there are several ways to approach the problem in different contexts:\n\n1. **Approximate Solutions**: You can approximate a square with the same area as a circle by using numerical methods or approximations of π. For example, if the radius of the circle is $ r $, the area is $ \\pi r^2 $, and the side length of the square would be $ \\sqrt{\\pi} r $.\n\n2. **Modern Tools**: With the help of modern computational tools or software (like GeoGebra, CAD programs, or even a calculator), you can construct a square with an area very close to that of a given circle.\n\n3. **Symbolic Representation**: In symbolic mathematics, you can represent the square with an area equal to that of a circle using the expression $ s = r\\sqrt{\\pi} $, where $ s $ is the side length of the square and $ r $ is the radius of the circle.\n\n4. **Historical and Philosophical Interest**: The problem has also been of interest in philosophy and mathematics as a symbol of the limits of human knowledge and the nature of infinity.\n\n### Summary\n- **Classical (Euclidean) Geometry**: Impossible.\n- **Modern Mathematics**: Can be approximated or represented symbolically.\n- **Practical Use**: You can construct a square with an area very close to that of a circle using numerical methods or technology.\n\nLet me know if you\'d like help with a specific approximation or calculation!', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='can you give me an example?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="Sure! Let's walk through an example of how to **approximate** squaring a circle using basic math.\n\n---\n\n### 🌟 Example: Square with the Same Area as a Circle\n\nLet’s say we have a **circle** with a **radius of 1 unit**.\n\n#### Step 1: Calculate the area of the circle\n$$\n\\text{Area of circle} = \\pi r^2 = \\pi \\times 1^2 = \\pi \\approx 3.1416\n$$\n\n#### Step 2: Find the side length of a square with the same area\n$$\n\\text{Area of square} = s^2 = \\pi\n$$\n$$\ns = \\sqrt{\\pi} \\approx \\sqrt{3.1416} \\approx 1.7725\n$$\n\n#### Step 3: Construct the square\n- Draw a line segment of length **1.7725 units**.\n- Use that segment as the side of a square.\n- The area of this square will be approximately equal to the area of the original circle.\n\n---\n\n### 📏 Summary of the Example\n- **Circle radius**: 1 unit  \n- **Circle area**: ≈ 3.1416 square units  \n- **Square side length**: ≈ 1.7725 units  \n- **Square area**: ≈ 3.1416 square units  \n\nSo, even though we can’t construct a perfect square with the same area as a circle using only a compass and straightedge, we can **approximate** it using modern math or tools.\n\nWould you like to try with a different radius or explore how to do this with a drawing tool like GeoGebra?", additional_kwargs={}, response_metadata={})]

Filtered History
================
[SystemMessage(content='You are a helpful assistant.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='Here is a summary of the previous\nconversation:\n\n"Squaring a circle is mathematically impossible using only a compass and straightedge due to π being a transcendental number, proven by Ferdinand von Lindemann in 1882. While classical construction is impossible, modern methods allow for approximations, symbolic representation, or digital tools to create a square with an area close to that of a given circle."\n', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='can you give me an example?', additional_kwargs={}, response_metadata={}),
 AIMessage(content="Sure! Let's walk through an example of how to **approximate** squaring a circle using basic math.\n\n---\n\n### 🌟 Example: Square with the Same Area as a Circle\n\nLet’s say we have a **circle** with a **radius of 1 unit**.\n\n#### Step 1: Calculate the area of the circle\n$$\n\\text{Area of circle} = \\pi r^2 = \\pi \\times 1^2 = \\pi \\approx 3.1416\n$$\n\n#### Step 2: Find the side length of a square with the same area\n$$\n\\text{Area of square} = s^2 = \\pi\n$$\n$$\ns = \\sqrt{\\pi} \\approx \\sqrt{3.1416} \\approx 1.7725\n$$\n\n#### Step 3: Construct the square\n- Draw a line segment of length **1.7725 units**.\n- Use that segment as the side of a square.\n- The area of this square will be approximately equal to the area of the original circle.\n\n---\n\n### 📏 Summary of the Example\n- **Circle radius**: 1 unit  \n- **Circle area**: ≈ 3.1416 square units  \n- **Square side length**: ≈ 1.7725 units  \n- **Square area**: ≈ 3.1416 square units  \n\nSo, even though we can’t construct a perfect square with the same area as a circle using only a compass and straightedge, we can **approximate** it using modern math or tools.\n\nWould you like to try with a different radius or explore how to do this with a drawing tool like GeoGebra?", additional_kwargs={}, response_metadata={})]

history system token usage: {'qwen3:8b': {'total_tokens': 1198, 'input_tokens': 1048, 'output_tokens': 150}}
chat token usage: {'qwen3:8b': {'total_tokens': 1872, 'input_tokens': 923, 'output_tokens': 949}}

total token usage: {'qwen3:8b': {'total_tokens': 3070, 'input_tokens': 1971, 'output_tokens': 1099}}
```
