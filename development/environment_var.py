import os
import sys

variables = {
    'RASA_NLU_MODEL_PATH': '/models/',
    'RASA_NLU_TRAINING_DATA_PATH': '/data/testDemo.json',
    'RASA_NLU_CONFIG_PATH': '/data/config_spacy.json',
    'RASA_NLU_MODEL_NAME': 'nlu_model',
    'RASA_CORE_TRAINING_DATA_PATH': '/data/stories.md',
    'RASA_CORE_MODEL_PATH': '/models/rasa_core_model',
    'RASA_CORE_DOMAIN_PATH': '/data/skype_domain.yml',
    'RASA_CORE_MAX_HISTORY': 5,
    'RASA_CORE_EPOCHS': 500,
    'RASA_CORE_BATCH_SIZE': 50,
    'RASA_CORE_VALIDATION': 0.2,
    'MINIMUM_TRAINING_INTENT_CONFIDENCE': 0.6,
    'MINIMUM_SUCCESSFUL_INTENT_CONFIDENCE': 0.2,
    #'QA_JSON': 'development/data/question_answer.json',
    #'DATABASE_URL':'',
    'INCIDENTS_PER_REQUEST':5
}
for k, v in variables.items():
    i = 'export {}="{}"'.format(k, v)
    os.system('echo {} >> {}'.format(i, sys.argv[1]))
