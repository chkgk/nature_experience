from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):
    def play_round(self):
        yield (pages.Decision, {'choose_b': random.choice([True, False])})

        if self.round_number == 1:
            yield (pages.Belief_choice_chance_1, {'choice_chance_1': random.randint(0, 100)})

        yield (pages.Belief_color, {'green_red': random.randint(0, 100)})
        yield (pages.Belief_other, {'a_or_b': random.randint(0, 100)})

        if not self.group.ball_green:
            assert self.player.room_payoff == c(0)
        else:
            if self.player.implement_b and self.player.other_choose_b:
                assert self.player.room_payoff == c(0)

            if self.player.implement_b and not self.player.other_choose_b:
                assert self.player.room_payoff == c(3)

            if not self.player.implement_b and self.player.other_choose_b:
                assert self.player.room_payoff == c(1)

            if not self.player.implement_b and not self.player.other_choose_b:
                assert self.player.room_payoff == c(1)

        if self.round_number == 2:
            assert self.player.payoff == self.player.in_round(self.player.relevant_round).room_payoff


        yield (pages.Results)

        if self.round_number == 1:
            assert "learned the outcome" in self.html
            yield (pages.Belief_choice_chance_2, {'choice_chance_2': random.randint(0, 100)})
