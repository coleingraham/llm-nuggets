from langchain_core.callbacks import UsageMetadataCallbackHandler

from utils import get_markdown_block_from_response


def developer(llm, task, previous_code=None, feedback=None, callbacks=None):
    prev = ''
    if previous_code:
        prev = """
here is your previous implementation:

```python
{code}
```""".format(code=previous_code)

    fb = ''
    if feedback:
        fb = """
here is the feedback on your previous code from QA:

"{fb}" """.format(fb=feedback)

    prompt = """you are a skilled python software developer.
you have been asked to develop software for the following task:

"{task}"
{prev}
{fb}

provide your python implementation. only output the python code inside
a markdown block.
    """.format(task=task, prev=prev, fb=fb)

    response = llm.invoke(prompt, config={'callbacks': callbacks})
    return get_markdown_block_from_response(response.content, 'python').strip()


def qa(llm, task, code, callbacks=None):
    prompt = """you are an expert QA engineer.
your team has been asked to develop code for the following task:

"{task}"

the developer has provided this implementation:

```python
{code}
```

provide suggestions to improve the code, if you have any.
only provide your suggestions. do not provide any updated code.
""".format(task=task, code=code)

    response = llm.invoke(prompt, config={'callbacks': callbacks})
    return response.content.strip()


RELEASE = 'RELEASE'
UPDATE = 'UPDATE'


def release_manager(llm, task, code, feedback, callbacks=None):
    prompt = f"""you are the release manager for a software development team.
your team has been asked to develop code for the following task:

"{task}"

the developer has provided this implementation:

```python
{code}
```

QA has provided the following feedback on the implementation:

"{feedback}"

is the current implementation good enough to release? or would it
truly benefit from the additional proposed changes? output {RELEASE}
or {UPDATE} for your answer. output only {RELEASE} or [UPDATE].
"""

    response = llm.invoke(prompt, config={'callbacks': callbacks})
    return response.content.strip()


def dev_team(llm, task, max_rounds=4, debug=False):
    code = None
    feedback = None

    dev_callback = UsageMetadataCallbackHandler()
    qa_callback = UsageMetadataCallbackHandler()
    rm_callback = UsageMetadataCallbackHandler()

    for i in range(max_rounds):
        if debug:
            print(f'Iteration: {i}', '\n')
        code = developer(llm, task, code, feedback, callbacks=[dev_callback])
        if debug:
            print(code, '\n')
        feedback = qa(llm, task, code, callbacks=[qa_callback])
        if debug:
            print(feedback, '\n')
        action = release_manager(llm,
                                 task,
                                 code,
                                 feedback,
                                 callbacks=[rm_callback])
        if debug:
            print(action, '\n')

        if action == RELEASE:
            break

    print('')
    print('      developer token usage:', dev_callback.usage_metadata)
    print('             qa token usage:', qa_callback.usage_metadata)
    print('release manager token usage:', rm_callback.usage_metadata)
    print('')
    return code


def test(llm):
    from langchain_core.callbacks import get_usage_metadata_callback
    with get_usage_metadata_callback() as cb:
        code = dev_team(llm,
                        'write a function to calculate the fibonacci sequence',
                        debug=True)
        print('=== Final Code ===')
        print(code)
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
