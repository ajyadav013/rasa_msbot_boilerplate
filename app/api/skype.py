import json
import requests
import sys
import os

CWD = os.path.dirname(os.path.realpath(__file__))
sys.path.append(CWD)
sys.path.append('/'.join(i for i in CWD.split('/')[:-1]))
from app.api.sessions import microsoft_bot_framework_connect

class SkypeAPI(object):
    """
    Sends reply via Skype
    """

    def get_headers(self, content_type):
        """
        Headers for the requests
        """
        # type - Text => dict
        # TODO - Add kwargs so that user can provide more headers
        Authorization = microsoft_bot_framework_connect()
        return {
            'content-type': content_type,
            'Authorization': Authorization if 'Bearer ' in Authorization else
            str('Bearer ' + Authorization)}

    def send_typing(self, ActivityRequestObject):
        """
        Send a 'typing' notification
        """
        try:
            headers = self.get_headers('application/json')
            ActivityResponseObject = {
                'type': 'typing',
                'from': {
                    'id': ActivityRequestObject['recipient']['id'],
                },
                'conversation': {
                    'id': ActivityRequestObject['conversation']['id'],
                    'name': 'convo1'
                },
                'recipient': {
                    'id': ActivityRequestObject['from']['id'],
                    'name': ActivityRequestObject['from']['name'],
                },
                'replyToId': ActivityRequestObject['id']
            }
            url = str(ActivityRequestObject['serviceUrl'] + 'v3/conversations/'
                      + ActivityRequestObject['conversation']['id']
                      + '/activities/' + ActivityRequestObject['id'])
            return requests.post(url, data=json.dumps(
                ActivityResponseObject), headers=headers)
        except Exception as e:
            print('Exception in skype api send_typing- ', e)

    def send_reply(self, ActivityRequestObject,
                   result_string, non_reply=False):
        """
        Send reply via Skype with appropriate parameters
        """
        try:
            print('Activity Request object',ActivityRequestObject)
            headers = self.get_headers('application/x-www-form-urlencoded')
            ActivityResponseObject = {
                'type': 'message',
                'from': {
                    'id': ActivityRequestObject['recipient']['id'],
                },
                'conversation': {
                    'id': ActivityRequestObject['conversation']['id'],
                    'name': 'convo1'
                },
                'recipient': {
                    'id': ActivityRequestObject['from']['id'],
                    'name': ActivityRequestObject['from']['name'],
                },
                'text': result_string,
                'replyToId': ActivityRequestObject['id']
            }
            if non_reply:
                url = str('/v3/conversations/' +
                          ActivityRequestObject['conversation']['id'] +
                          '/activities')
            else:
                url = str(ActivityRequestObject['serviceUrl'] +
                          'v3/conversations/'
                          + ActivityRequestObject['conversation']['id']
                          + '/activities/' + ActivityRequestObject['id'])
            return requests.post(url, data=json.dumps(
                ActivityResponseObject), headers=headers)
        except Exception as e:
            print('Exception in skype api send_reply- ', e)

    def send_form(self, ActivityRequestObject):
        """
        Send Form
        """
        try:
            headers = self.get_headers('application/x-www-form-urlencoded')
            ActivityResponseObject = {
                'type': 'message',
                'from': {
                    'id': ActivityRequestObject['recipient']['id'],
                },
                'conversation': {
                    'id': ActivityRequestObject['conversation']['id'],
                    'name': 'convo1'
                },
                'recipient': {
                    'id': ActivityRequestObject['from']['id'],
                    'name': ActivityRequestObject['from']['name'],
                },
                'text': 'Here is blah blah blah',
                'attachments': [
                    {
                        'contentType': """application/
                        vnd.microsoft.card.adaptive""",
                        'content': {
                            '$schema': """http://adaptivecards.io/
                            schemas/adaptive-card.json""",
                            'type': 'AdaptiveCard',
                            'version': '1.0',
                            'body': [
                                {
                                    'type': 'Input.Number',
                                    'id': 'number',
                                    'placeholder': 'Enter number'
                                }
                            ],
                            'actions': [
                                {
                                    'type': 'Action.Http',
                                    'method': 'POST',
                                    'url': """https://amazatic-ml.herokuapp.com/
                                    bot""",
                                    'title': 'OK'
                                }
                            ]
                        }
                    }
                ],
                'replyToId': ActivityRequestObject['id']
            }
            url = str(ActivityRequestObject['serviceUrl'] + 'v3/conversations/'
                      + ActivityRequestObject['conversation']['id']
                      + '/activities/' + ActivityRequestObject['id'])
            return requests.post(url, data=json.dumps(
                ActivityResponseObject), headers=headers)
        except Exception as e:
            print('Exception in skype api send_form- ', e)

    def start_conversation(self, bot_id, bot_name,
                           member_list, topic_name, isGroup):
        """
        Start Conversation and set appropriate
        parameters for the ActivityRequestObject
        """
        ActivityResponseObject = {
            'bot': {
                'id': bot_id,
                'name': bot_name
            },
            'isGroup': isGroup,
            'members': [
                {
                    'id': member_id,
                    'name': mamber_name
                } for member in member_list],
            'topicName': topic_name
        }
        url = str('https://smba.trafficmanager.net/apis/v3/conversations')
        headers = self.get_headers(
            'application/json', ('Bearer ' + token['access_token']))
        return requests.post(url, data=json.dumps(
            ActivityResponseObject), headers=headers)

    def send_media_message(self, ActivityRequestObject,
                           attachment_type, attachment_Url, attachment_name):
        """
        Send Media Message as a reply via Skype
        """
        ActivityResponseObject = {
            'type': 'message',
            'from': {
                'id': ActivityRequestObject['recipient']['id'],
            },
            'conversation': {
                'id': ActivityRequestObject['conversation']['id'],
                'name': 'convo1'
            },
            'recipient': {
                'id': ActivityRequestObject['from']['id'],
                'name': ActivityRequestObject['from']['name'],
            },
            'text': result_string,
            'attachments': [
                {
                    'contentType': attachment_type,
                    'contentUrl': attachment_Url,
                    'name': attachment_name
                }
            ],
            'replyToId': ActivityRequestObject['id']
        }
        url = str(ActivityRequestObject['serviceUrl'] + 'v3/conversations/'
                  + ActivityRequestObject['conversation']['id']
                  + '/activities/' + ActivityRequestObject['id'])
        return requests.post(url, data=json.dumps(
            ActivityResponseObject), headers=headers)

    def send_suggestions(self, ActivityRequestObject, question):
        '''
            Ask user to select one of suggestions.
            suggestions: type - list(dict())
                ex - [{'type': '','title': '','value': ''}]
        '''
        headers = self.get_headers('application/json')
        ActivityResponseObject = {
            "type": "message",
            "from": {
                "id": ActivityRequestObject["recipient"]["id"],
            },
            "conversation": {
                "id": ActivityRequestObject["conversation"]["id"],
                "name": "convo1"
            },
            "recipient": {
                "id": ActivityRequestObject["from"]["id"],
                "name": ActivityRequestObject["from"]["name"],
            },
            "text": """I have colors in mind,
            but need your help to choose the best one.""",
            "inputHint": "expectingInput",
            "suggestedActions": {
                "actions": [
                    {
                        "type": "imBack",
                        "title": "Blue",
                        "value": "Blue"
                    },
                    {
                        "type": "imBack",
                        "title": "Red",
                        "value": "Red"
                    },
                    {
                        "type": "imBack",
                        "title": "Green",
                        "value": "Green"
                    }
                ]
            },
            "replyToId": ActivityRequestObject["id"]
        }
        url = str(ActivityRequestObject['serviceUrl'] + 'v3/conversations/'
                  + ActivityRequestObject['conversation']['id']
                  + '/activities/' + ActivityRequestObject['id'])
        return requests.post(url, data=json.dumps(
            ActivityResponseObject), headers=headers)

    def send_rich_cards(self, title, subtitle,
                        description,
                        image_url, image_title,
                        button_type, button_url, button_image, button_title):
        """
        Send Rich Cards
        """
        ActivityResponseObject = {
            'type': 'message',
            'from': {
                'id': ActivityRequestObject['recipient']['id'],
            },
            'conversation': {
                'id': ActivityRequestObject['conversation']['id'],
                'name': 'convo1'
            },
            'recipient': {
                'id': ActivityRequestObject['from']['id'],
                'name': ActivityRequestObject['from']['name'],
            },
            'text': result_string,
            'attachments': [
                {
                    'contentType': 'application/vnd.microsoft.card.hero',
                    'content': {
                        'title': title,
                        'subtitle': subtitle,
                        'text': description,
                        'images': [
                            {
                                'url': image_url,
                                'alt': image_title,
                                'tap': {
                                    'type': '',
                                    'value': ''
                                }
                            }
                        ],
                        'buttons': [
                            {
                                'type': button_type,
                                'title': button_title,
                                'image': button_image,
                                'value': button_url
                            }
                        ]
                    }
                }
            ],
            'replyToId': ActivityRequestObject['id']
        }
        url = str(ActivityRequestObject['serviceUrl'] + 'v3/conversations/'
                  + ActivityRequestObject['conversation']['id']
                  + '/activities/' + ActivityRequestObject['id'])
        return requests.post(url, data=json.dumps(
            ActivityResponseObject), headers=headers)
