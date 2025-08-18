# llm-nuggets

Various minimalist examples of how to work with LLMs programmatically meant for
educational purposes.

# Motivation

I routinely train people how to use LLMs in various contexts: from curious
indivuals to engineering teams at large corporations. My focus is always to
teach what is actually happening rather than simply how to use fancy libraries
and thinking that it's magic. My hope is that these examples help demystify
some of the concepts that arise when working with LLMs and act as an easier
entry point to learning how the sausage is made with many popular libraries.


# Usage

The only non standard dependency for these examples is
[langchain](https://pypi.org/project/langchain/). This is solely because I
wanted to make it easy to use any LLM, local or API, with these examples with
no code changes. Effectively langchain is just an abstraction. I am not
demonstrating anything that cannot be done with a specific LLM wrapper library,
of even with [curl](https://curl.se/) for that matter. Again: no magic here.

However, since I did write these examples using langchain, there are a few
things you need to know about. First, depending on the specific LLM you are
using, you will need to install the appropriate langchain sub package. I
personally used [langchain-ollama](https://pypi.org/project/langchain-ollama/)
to run what I have, but if you want to use anything else you need to install
the appropriate library and possibly setup the needed environment variables.

The provided scripts all pass command line arguments to the langchain
[init_chat_model](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html)
function. Specifically `--provider` and `--model` are required when running
these on your own (as previously stated, you need to make sure you have setup
whatever requirements for your particular model first).

# Examples

* [Misc](docs/0_misc.md): descriptions of various helper code
* [Basic Chat Wrapper](docs/1_simple_chat.md): a simple example of managing chat history
* [Filtering Chat History](docs/2_filtered_history.md): sending only a specified number of messages per request
* [Simplistic ChatGPT Style Memory System Clone](docs/3_memory_system.md): using a LLM to extract memorable facts from user messages for use in future conversations
* [Chat History Summarization](docs/4_summarize_history.md): creates a running summary of older messages to reduce context
