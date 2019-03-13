from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.group.ball_green:
            if self.player.action and self.player.others_action:
                assert self.player.room_payoff == c(0)
            elif self.player.action and not self.player.others_action:
                assert self.player.room_payoff == c(3)
            elif not self.player.action and self.player.others_action:
                assert self.player.room_payoff == c(1)
            else:
                assert self.player.room_payoff == c(1)
        else:
            assert self.player.room_payoff == c(0)
        yield (pages.Results)
