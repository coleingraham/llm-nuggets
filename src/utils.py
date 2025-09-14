import os
import json
import logging
import re


logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))
LOG = logging.getLogger()


def get_markdown_block_from_response(response, what=''):
    """Given a string that should contain a markdown block and optionally the
    type of code it is, extract the contents of the first markdown block, or
    throw an error if there isn't one because yolo.
    """
    pattern = f'```{what}(.*?)```'
    matches = re.findall(pattern, response, re.DOTALL)
    return matches[0]


def get_json_from_response(response):
    """Specifically tries to extract JSON from markdown in the provided string.
    """
    return json.loads(get_markdown_block_from_response(response, 'json'))
