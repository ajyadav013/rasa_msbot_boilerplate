import json
import os
import sys

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

from app.output_channel import OutputChannel
from app.api.skype import SkypeAPI
CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.append('/'.join(i for i in CWD.split('/')[:-1]))

RASA_NLU_MODEL_PATH = CWD + os.environ.get('RASA_NLU_MODEL_PATH')
RASA_NLU_MODEL_NAME = os.environ.get('RASA_NLU_MODEL_NAME')
RASA_CORE_MODEL_PATH = CWD + os.environ.get('RASA_CORE_MODEL_PATH')
QA_JSON = os.environ.get('QA_JSON')

class Bot():
    """
    Bot class to Process Data
    """

    def __init__(self):
        self.agent = Agent.load(
            RASA_CORE_MODEL_PATH,
            interpreter=RasaNLUInterpreter(RASA_NLU_MODEL_PATH + RASA_NLU_MODEL_NAME))
        self.data = None
        self.channel = None

        with open(QA_JSON, 'r') as handle:
            self.question_answer = json.load(handle)

    def on_post(self, req, resp):
        """
        pass the data(user message) to RASA for
        processing and send the result as a message via Skype API
        """
        try:
            reply = SkypeAPI()
            self.data = req.context['request']
            if self.data['user'] is not None:
                self.user_id = self.data['from']['id'][3:]
                self.channel = self.data['channelId']
                self.agent.handle_message(self.data['text'], None, OutputChannel(self.data))
        except Exception as e:
            print("Exception in bot- ", e)
