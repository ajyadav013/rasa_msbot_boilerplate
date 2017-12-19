import requests
import difflib
import os
import inspect

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from app.models.user import Users

INCIDENTS_PER_REQUEST = os.environ.get('INCIDENTS_PER_REQUEST')

def resetTracker(tracker):
    """
    Reset all slots to None
    """
    for slot in tracker.slots:
        return [SlotSet(slot, None) for slot in tracker.slots]

def sendPredefinedMessage(dispatcher,intent=None):
    """
    Print the predefined messages in the pickle file
    """
    try:
        from app.main import bott
        que_array = list(bott.question_answer[intent].keys())
        que_result = difflib.get_close_matches(bott.data['text'], que_array, cutoff=0.1)
        description = bott.question_answer[intent][que_result[0]]
        dispatcher.utter_message('{}'.format(description))
    except Exception as e:
        dispatcher.utter_message('Hello, How may I help you?')
        print('Exception in sendPredefinedMessage -', e)

class ActionUtterGreet(Action):
    """
        Respond to greet intent
    """
    def name(self):
        return 'action_utter_greet'

    def run(self, dispatcher, tracker, domain):
        try:
            sendPredefinedMessage(dispatcher, intent='greet')
            return resetTracker(tracker)

        except Exception as e:
            print('Exception in greet -', e)

class ActionUtterGoodbye(Action):
    """
    Respond to goodbye intent
    """
    def name(self):
        return 'action_utter_goodbye'

    def run(self, dispatcher, tracker, domain):
        try:
            print('Inside goodbye action')
            sendPredefinedMessage(dispatcher, intent='goodbye')
            return resetTracker(tracker)

        except Exception as e:
            print('Exception in greet -', e)
class ActionUtterContact(Action):
    """
    Respond to contact intent
    """
    def name(self):
        return 'action_utter_contact'

    def run(self, dispatcher, tracker, domain):
        try:
            print('Inside contact action')
            description = "Hi, you can contact me on my email - ".format(os.environ.get('COMMON_CONTACT_EMAIL'))
            dispatcher.utter_message(description)
            return resetTracker(tracker)

        except Exception as e:
            print('Exception in contact -', e)
