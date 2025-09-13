from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


def chat(llm, messages, prompt):
    messages = messages.copy()
    messages.append(HumanMessage(prompt))
    response = llm.invoke(messages)
    content = response.content
    messages.append(AIMessage(content))
    return messages


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback
    with get_usage_metadata_callback() as cb:
        messages = [SystemMessage('you are very funny')]
        messages = chat(llm, messages, 'tell me a joke')
        messages = chat(llm, messages, 'tell me another')
        pprint(messages)
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
