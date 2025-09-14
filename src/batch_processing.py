from typing import List
from langchain_core.messages import HumanMessage, SystemMessage


def sentiment_analysis(llm, text: str):
    messages = [
        SystemMessage("""You will be provided with some text, and your task is
to classify its sentiment as positive, neutral, or negative  with no
punctuation."""),
        HumanMessage(text)]
    response = llm.invoke(messages)
    return response.content.strip().lower()


def batch_sentiment_analysis(llm, texts: List[str]):
    text = "\n".join(texts)
    messages = [
        SystemMessage(""""You will be provided with some text, and your task is
to classify its sentiment as positive, neutral, or negative. Each example will
be on a new line. For each example, provide the sentiment on its own line."""),
        HumanMessage(text)]
    response = llm.invoke(messages)
    return [x.strip().lower() for x in response.content.split('\n')]


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback
    texts = ["I love programming.",
             "I don't like how humid it is",
             "how are you?"]

    print('=== Multiple Requests ===')
    with get_usage_metadata_callback() as cb:
        results = []
        for text in texts:
            results.append({'input': text,
                            'output': sentiment_analysis(llm, text)})
        pprint(results)

    print('\ntotal token usage:', cb.usage_metadata)
    print('')
    print('=== Batched Request ===')
    with get_usage_metadata_callback() as cb:
        results = [{'input': t, 'output': s}
                   for t, s in zip(texts, batch_sentiment_analysis(llm, texts))]
        pprint(results)
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
