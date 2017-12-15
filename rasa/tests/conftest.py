from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import matplotlib
import pytest

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleOutputChannel
from rasa_core.dispatcher import Dispatcher
from rasa_core.domain import TemplateDomain
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.slots import Slot
from rasa_core.tracker_store import InMemoryTrackerStore

matplotlib.use('Agg')

logging.basicConfig(level="DEBUG")

DEFAULT_DOMAIN_PATH = "data/test_domains/default_with_slots.yml"

DEFAULT_STORIES_FILE = "data/dsl_stories/stories_defaultdomain.md"


class CustomSlot(Slot):
    def as_feature(self):
        return [0.5]


@pytest.fixture(scope="session")
def default_domain():
    return TemplateDomain.load(DEFAULT_DOMAIN_PATH)


@pytest.fixture(scope="session")
def default_agent(default_domain):
    agent = Agent(default_domain,
                  policies=[MemoizationPolicy()],
                  interpreter=RegexInterpreter(),
                  tracker_store=InMemoryTrackerStore(default_domain))
    agent.train(DEFAULT_STORIES_FILE)
    return agent


@pytest.fixture
def default_dispatcher(default_domain):
    bot = ConsoleOutputChannel()
    return Dispatcher("my-sender", bot, default_domain)
