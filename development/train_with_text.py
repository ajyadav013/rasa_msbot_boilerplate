from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import sys
import os

from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.channels import UserMessage
from rasa_core.channels.console import ConsoleOutputChannel, ConsoleInputChannel
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.append('/'.join(i for i in CWD.split('/')[:-1]))
from app.config import *
logger = logging.getLogger(__name__)


def run_fake_user(input_channel, max_training_samples=10, serve_forever=True):
    logger.info("Starting to train policy")
    agent = Agent(RASA_CORE_DOMAIN_PATH,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=RegexInterpreter())

    agent.train_online(RASA_CORE_TRAINING_DATA_PATH,
                       input_channel=input_channel,
                       epochs=RASA_CORE_EPOCHS,
                       max_training_samples=max_training_samples)

    while serve_forever:
        agent.handle_message(UserMessage(back, ConsoleOutputChannel()))

    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")

    if len(sys.argv) < 2 or sys.argv[1] == 'scratch':
        max_training_samples = 10
    elif sys.argv[1] == 'pretrained':
        max_training_samples = -1
    else:
        raise Exception("Choose from pretrained or training from scratch")

    run_fake_user(ConsoleInputChannel(), max_training_samples)
