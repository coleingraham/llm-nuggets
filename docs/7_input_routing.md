# Few-shot Prompting as a Router

There are many instances where a system expects a specific thing,
such as a single question to search for, a single task to accomplish,
etc. However users of LLMs are used to being able to explain what they
want, ask for multiple things at once, provide background information,
and so on. This presents a problem if you directly take the user's input
and use it to perform a database search. There could be confusing,
contradictory, or irrelevant text that ultimately degrades your search
results.

This example provides a basic approach to taking user input and extracting
portions of it in a described format. There are two cases demonstrated:

1. extracting questions and associated dates for searching a database
2. deciding which route(s) user input should be sent to

Both cases are handled through few-shot prompting, where examples of
the input and expexted output are provided as initial messages. Additionally
a system prompt is used to tell the model to only output JSON in the requested
format, and to provide the current date, which is useful for addressing relative
times in requests (e.g. "what will be the date two weeks from Wednesday?").

# Example Usage

```
$ cd src
$ python input_routing.py --provider ollama --model qwen3:8b --temperature 0.3

[HumanMessage(content='you only answer questions about companies.\nall dates used in the "quarters" key should be in the format YYYYQ#.', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='what was revenue in 2020Q1?\nhow popular is the music library?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='\n{\n    "questions": [\n        {\n            "question": "what was revenue?",\n            "quarters": ["2020Q1"]\n        },\n        {\n            "question": "how popular is the music library?",\n            "quarters": []\n        }\n    ]\n}\n', additional_kwargs={}, response_metadata={}),
 HumanMessage(content='Hello, how are you?', additional_kwargs={}, response_metadata={}),
 AIMessage(content='{"questions": []}', additional_kwargs={}, response_metadata={})]

User Input: what was the company saying about AI in four years ago?
and what about the music library at that time?
{'questions': [{'quarters': ['2021Q1'],
                'question': 'what was the company saying about AI?'},
               {'quarters': ['2021Q1'],
                'question': 'what about the music library at that time?'}]}
User Input: what is the weather today in NYC?
{'questions': []}

=== New Task ===
[HumanMessage(content='your job is to identify individual requests\nand assign each to a particular type. the types of input supported are:\n\n* transcript_search: conversations related to the state of or questions about public companies\n* food: questions about food, recipies, meals, etc.\n* dev_team: requests for developing software\n* data_analysis: requests regarding the analysis of data\n* chat: all other topics', additional_kwargs={}, response_metadata={}),
 HumanMessage(content="I'm hungry. also, what did the company say\nabout AI?", additional_kwargs={}, response_metadata={}),
 AIMessage(content='[\n    {"input": "I\'m hungry.", "type": "food"},\n    {"input": "what did the company say about AI?", "type": "transcript_search"}\n]\n', additional_kwargs={}, response_metadata={})]

User Input: what should I eat??
{'input': 'what should I eat??', 'type': 'food'}
User Input: what is the weather today in NYC? also write hello world in python.
[{'input': 'what is the weather today in NYC?', 'type': 'chat'},
 {'input': 'write hello world in python', 'type': 'dev_team'}]

total token usage: {'qwen3:8b': {'total_tokens': 1084, 'input_tokens': 952, 'output_tokens': 132}}
```
