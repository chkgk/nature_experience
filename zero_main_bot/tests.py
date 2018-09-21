from otree.api import Currency as c
from . import pages
from ._builtin import Bot

import random


class PlayerBot(Bot):
    # cases = ['A', 'B']

    def play_round(self):
        decision = random.random() <= 0.4

        # decision = {
        #     'A': False,
        #     'B': True,
        # # }[self.case]
        # }[random.choice(['A', 'B'])]

        yield (pages.Decision, {'choose_b': decision})
        if not self.player.ball_green:
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

        if self.round_number == 1:
            yield (pages.Belief_choice_chance_1, {'choice_chance_1': random.randint(0, 100)})

        yield (pages.Belief_color, {'green_red': random.randint(0, 100)})
        yield (pages.Belief_other, {'a_or_b': random.randint(0, 100)})
        yield (pages.Results)

        if self.round_number == 1:
            assert "learned the outcome" in self.html
            yield (pages.Belief_choice_chance_2, {'choice_chance_2': random.randint(0, 100)})