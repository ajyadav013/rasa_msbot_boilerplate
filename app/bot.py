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
            print('reply', reply)
            self.data = req.context['request']
            print('self.data in bot', self.data, self.data['user'])
            if self.data['user'] is not None:
                print('inside self.data')
                self.user_id = self.data['from']['id'][3:]
                print('inside self.data after assigniong user id')
                self.channel = self.data['channelId']
                print('inside self.data after assigning channel')
                print('Agent', self.agent)
                #reply.send_typing(self.data) #Commented because it raise double response problem
                check_default = self.agent.handle_message(self.data['text'], None, OutputChannel(self.data))
                print('Check default', check_default)
                # check_default = self.agent.handle_message(
                #     self.data['text'], None,
                #     OutputChannel(self.data))
                if check_default: # Check default sometimes is returned None by processor.handle_message
                    if (check_default[0] is False):  # The result found by rasa
                        # is below the confidence level set
                        reply.send_reply(self.data, check_default[1])
        except Exception as e:
            print("Exception in bot- ", e)
