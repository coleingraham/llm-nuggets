# Processing Multiple Inputs in One Request

It is often needed to use a LLM to do some form of data processing or
information extraction. The most obvious way to do this is to construct
a prompt that takes one input and produces one output. While this does work,
you end up paying for the entire base prompt for every use. If your use case
is in-line then this is the best you can do. However if you are able to batch
process your inputs, you can often save a non trivial amount of input tokens
for the exact same result just by restructuring your prompt to work on multiple
inputs at once.

# Example Usage

```
$ cd src
$ python batch_processing.py --provider ollama --model qwen3:8b --temperature 0.3

=== Multiple Requests ===
[{'input': 'I love programming.', 'output': 'positive'},
 {'input': "I don't like how humid it is", 'output': 'negative'},
 {'input': 'how are you?', 'output': 'neutral'}]

total token usage: {'qwen3:8b': {'total_tokens': 178, 'input_tokens': 172, 'output_tokens': 6}}

=== Batched Request ===
[{'input': 'I love programming.', 'output': 'positive'},
 {'input': "I don't like how humid it is", 'output': 'negative'},
 {'input': 'how are you?', 'output': 'neutral'}]

total token usage: {'qwen3:8b': {'input_tokens': 85, 'output_tokens': 6, 'total_tokens': 91}}
```
