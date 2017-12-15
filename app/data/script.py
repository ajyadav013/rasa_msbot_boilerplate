import json


with open('testDemo.json', 'r') as f:
    a = json.load(f)


valid = ['greet', 'affirm', 'deny', 'negative', 'thanks', 'goodbye']
    
for i in  a['rasa_nlu_data']['common_examples']:
    if i['intent'] in valid:
        print(i)
