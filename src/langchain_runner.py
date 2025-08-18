import argparse
from langchain.chat_models import init_chat_model


def get_llm(provider,
            model_name,
            temperature=0,
            reasoning=False):
    """Wrapper for creating the requested LLM. Note that you need the correct
    libraries installed for whatever model you plan on using. Additionally
    for API models, the appropriate environment variables must be set."""
    return init_chat_model(f'{provider}:{model_name}',
                           temperature=temperature,
                           reasoning=reasoning)


def get_argparser():
    """Parse the LLM arguments from the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--provider',
            help='model provider')
    parser.add_argument(
            '--model',
            help='model name')
    parser.add_argument(
            '--temperature',
            default=0.0,
            help='temperature')
    parser.add_argument(
            '--reasoning',
            action='store_true',
            help='turn on reasoning')
    return parser.parse_args()


def get_llm_from_args():
    """Glue together making the argument parser and creating the LLM."""
    args = get_argparser()
    return get_llm(args.provider,
                   args.model,
                   temperature=float(args.temperature),
                   reasoning=args.reasoning)


if __name__ == '__main__':
    LLM = get_llm_from_args()
    print(LLM.invoke('hi'))
