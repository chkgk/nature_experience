from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from otree.api import Submission
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield Submission(pages.FakeGrouping, check_html=False)
        assert self.player.action
        if self.player.ball_green:
            if self.player.others_action:
                assert self.player.room_payoff == c(0)
            else:
                assert self.player.room_payoff == c(3)
        else:
            assert self.player.room_payoff == c(0)

        yield (pages.Results)
