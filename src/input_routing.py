from datetime import date
import json
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


def handle_input(llm, user_input, examples):
    today = date.today().isoformat()
    messages = [SystemMessage(f'''
You are an AI attempting to help someone. Today is {today}.
For any questions being asked, if and only if they are
possibly related the ongoing conversation, break the request
into individual questions in the format requested. Your output
must be a JSON object. Only output the JSON object''')]
    messages.extend(examples)
    messages.append(HumanMessage(user_input))
    response = llm.invoke(messages)
    return json.loads(response.content)


def test(llm):
    from pprint import pprint
    from langchain_core.callbacks import get_usage_metadata_callback
    with get_usage_metadata_callback() as cb:
        examples = [HumanMessage('''you only answer questions about companies.
all dates used in the "quarters" key should be in the format YYYYQ#.'''),

                    HumanMessage('''what was revenue in 2020Q1?
how popular is the music library?'''),
                    AIMessage('''
{
    "questions": [
        {
            "question": "what was revenue?",
            "quarters": ["2020Q1"]
        },
        {
            "question": "how popular is the music library?",
            "quarters": []
        }
    ]
}
'''),
                    HumanMessage('Hello, how are you?'),
                    AIMessage('{"questions": []}')]

        pprint(examples)
        print('')
        user_input = '''what was the company saying about AI in four years ago?
and what about the music library at that time?'''
        print('User Input:', user_input)
        pprint(handle_input(llm,
                            user_input,
                            examples))

        user_input = 'what is the weather today in NYC?'
        print('User Input:', user_input)
        pprint(handle_input(llm,
                            user_input,
                            examples))

        print('\n=== New Task ===')
        examples = [HumanMessage('''your job is to identify individual requests
and assign each to a particular type. the types of input supported are:

* transcript_search: conversations related to the state of or questions about public companies
* food: questions about food, recipies, meals, etc.
* dev_team: requests for developing software
* data_analysis: requests regarding the analysis of data
* chat: all other topics'''),
                    HumanMessage("""I'm hungry. also, what did the company say
about AI?"""),
                    AIMessage('''[
    {"input": "I'm hungry.", "type": "food"},
    {"input": "what did the company say about AI?", "type": "transcript_search"}
]
''')]

        pprint(examples)
        print('')
        user_input = 'what should I eat??'
        print('User Input:', user_input)
        pprint(handle_input(llm,
                            user_input,
                            examples))

        user_input = 'what is the weather today in NYC? also write hello world in python.'
        print('User Input:', user_input)
        pprint(handle_input(llm,
                            user_input,
                            examples))
    print('\ntotal token usage:', cb.usage_metadata)


if __name__ == '__main__':
    from langchain_runner import get_llm_from_args
    LLM = get_llm_from_args()
    test(LLM)
