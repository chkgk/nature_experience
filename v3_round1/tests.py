from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random

from django.conf import settings

class PlayerBot(Bot):

    def play_round(self):

        print(settings.DEBUG)

        if self.player.aa_treatment:
            yield (pages.DecisionInfo)
            yield (pages.DecisionAssignment)

        if self.player.ra_treatment:
            yield (pages.Decision, {'action1_b': random.choice([True, False])})

        yield (pages.Belief_color, {'green_red': random.randint(0, 100)})
        yield (pages.Belief_other, {'a_or_b': random.randint(0, 100)})