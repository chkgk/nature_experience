from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):
        edu = random.randint(0, 5)
        survey = {
            "age": random.randint(18, 60),
            "gender": random.choice(['Male', 'Female', 'Other', 'I prefer not to tell']),
            "education": edu,
            "major": "" if edu < 2 else random.choice(["econ", "other"]),
            "risk": random.randint(0, 10),
        }

        yield (pages.Survey, survey)
        yield (pages.LastPage)
