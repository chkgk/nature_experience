from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from otree.api import Submission
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield Submission(pages.FakeGrouping, check_html=False)
        yield (pages.Results)
