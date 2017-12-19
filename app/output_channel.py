from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import six
from builtins import input
from typing import Text

from rasa_core.channels.channel import UserMessage
from rasa_core.channels.channel import InputChannel, OutputChannel
from rasa_core.utils import bcolors, print_color

from app.api.skype import SkypeAPI


class OutputChannel(OutputChannel):
    """
    Simple bot that outputs the bots messages back to skype/slack etc.
    """

    default_output_color = bcolors.OKBLUE

    def __init__(self, data):
        self.data = data
        self.reply = self.setOutputInstance(data)

    def send_text_message(self, recipient_id, message):
        # type: (Text, Text) -> None
        try:
            self.reply.send_reply(self.data, message)
        except Exception as e:
            print('Exception in send_text_message -', e)

    def setOutputInstance(self, data):
        print('Inside output channel setOutputInstance method data', data)
        if data['channelId'] == 'skype':
            return SkypeAPI()
        else:
            pass


class ConsoleInputChannel(InputChannel):
    """
    Input channel that reads the user messages from the command line.
    """

    def __init__(self, data):
        self.data = data

    def _record_messages(self, on_message, max_message_limit=None):
        if six.PY2:
            # in python 2 input doesn't return unicode values
            self.text = self.text.decode("utf-8")
        try:
            on_message(UserMessage(
                self.data["text"], ConsoleOutputChannel(self.data)))
        except Exception as e:
            # on_message(UserMessage('Error message',
            # ConsoleOutputChannel(self.data)))
            print("Exception in channel- ", e)
            pass  # will resolve this later based
        # on the default message to print when error occurs

    def start_async_listening(self, message_queue):
        self._record_messages(message_queue.enqueue)

    def start_sync_listening(self, message_handler):
        self._record_messages(message_handler)
