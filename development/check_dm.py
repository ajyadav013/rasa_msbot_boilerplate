from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import sys

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.rest import HttpInputChannel

CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.append('/'.join(i for i in CWD.split('/')[:-1]))
RASA_CORE_MODEL_PATH = CWD + os.environ.get('RASA_CORE_MODEL_PATH')
RASA_NLU_MODEL_PATH = CWD + os.environ.get('RASA_NLU_MODEL_PATH')
RASA_NLU_MODEL_NAME = os.environ.get('RASA_NLU_MODEL_NAME')

agent = Agent.load(
    RASA_CORE_MODEL_PATH,
    interpreter=RasaNLUInterpreter(
        RASA_NLU_MODEL_PATH + RASA_NLU_MODEL_NAME
    )
)

def run_application(serve_forever=True):
    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    run_application()
