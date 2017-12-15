import requests
import json
import os
import datetime
from app.models.logging import Logging

def generateNluModel():
    """
        Generate NLU stories from logs in database
    """
    try:
        logs = Logging.select()
        with open('/app/training.json', 'w+') as fd:
            for i in range(len(logs)):
                jsn = {"text":logs[i].text, "intent":logs[i].intent}
                json.dump(jsn, fd)
        os.system('less /app/training.json')
    except Exception as e:
        print("Exception in logging ", e)

if __name__ == '__main__':
    generateNluModel()

