from otree.api import Currency as c, currency_range, SubmissionMustFail, Submission
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Decision, {"action2_b": random.choice([True, False])})
        yield (pages.Belief_color, {"green_red": random.randint(0, 100)})
        yield (pages.Belief_other, {"a_or_b": random.randint(0, 100)})
        yield (pages.Motivation, {"motivation": random.randint(1,5), "motivation_other": ""})
        yield Submission(pages.FakeWait, check_html=False)
