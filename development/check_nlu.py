import os
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

import sys

CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.append('/'.join(i for i in CWD.split('/')[:-1]))

RASA_NLU_CONFIG_PATH = CWD + os.environ.get('RASA_NLU_CONFIG_PATH')
RASA_NLU_MODEL_PATH = CWD + os.environ.get('RASA_NLU_MODEL_PATH')
RASA_NLU_MODEL_NAME = os.environ.get('RASA_NLU_MODEL_NAME')

metadata = Metadata.load(RASA_NLU_MODEL_PATH + RASA_NLU_MODEL_NAME)
interpreter = Interpreter.load(metadata, RasaNLUConfig(RASA_NLU_CONFIG_PATH))
print(interpreter.parse(sys.argv[1]))
