from otree.api import Currency as c, currency_range, Submission, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    # cases = ['no_timeouts', 'decision_timeout', 'feelings_timeout']
    cases = ['no_timeouts']

    def check_room_payoffs(self):
        assert "None" not in self.html
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


    def play_round(self):
        choose_b = random.random() <= 0.4
        if self.case == 'no_timeouts':
            yield (pages.Decision, {'choose_b': choose_b})

            if self.round_number == 1:
                yield (pages.Belief_choice_chance_1, {'choice_chance_1': random.randint(0, 100)})

            yield (pages.Belief_color, {'green_red': random.randint(0, 100)})
            yield (pages.Belief_other, {'a_or_b': random.randint(0, 100)})

            self.check_room_payoffs()

            if self.round_number == 2:
                assert self.player.payoff == self.player.in_round(self.player.relevant_round).room_payoff


            yield (pages.Results)

            if self.round_number == 1:
                assert "learned the outcome" in self.html
                yield (pages.Belief_choice_chance_2, {'choice_chance_2': random.randint(0, 100)})

        if self.case == 'decision_timeout':
            if self.round_number == 1:
                if self.player.id_in_group == 1:
                    yield Submission(pages.Decision, {}, timeout_happened=True)
                else:
                    yield (pages.Decision, {'choose_b': random.choice([True, False])})

                    yield (pages.Belief_choice_chance_1, {'choice_chance_1': random.randint(0, 100)})

                    yield (pages.Belief_color, {'green_red': random.randint(0, 100)})
                    yield (pages.Belief_other, {'a_or_b': random.randint(0, 100)})

                    yield(pages.DropoutOther)

            if self.round_number == 2:
                if self.player.in_round(1).id_in_group == 1:
                    assert "You took too long" in self.html
                    yield (pages.DropoutExit)

                if self.player.in_round(1).id_in_group != 1:
                    # this guy goes straight to last page.
                    pass

        if self.case == 'feelings_timeout':
            if self.round_number == 1:
                yield (pages.Decision, {'choose_b': choose_b})

                if self.player.id_in_group == 1:
                    yield Submission(pages.Belief_choice_chance_1, {}, timeout_happened=True)
                else:
                    yield (pages.Belief_choice_chance_1, {'choice_chance_1': random.randint(0, 100)})

                    yield (pages.Belief_color, {'green_red': random.randint(0, 100)})
                    yield (pages.Belief_other, {'a_or_b': random.randint(0, 100)})

                    self.check_room_payoffs()

                    yield(pages.Results)
                    yield (pages.Belief_choice_chance_2, {'choice_chance_2': random.randint(0, 100)})

            if self.round_number == 2:
                if self.player.in_round(1).id_in_group == 1:
                    assert "You took too long" in self.html
                    yield (pages.DropoutExit)

                if self.player.in_round(1).id_in_group != 1:
                    yield (pages.Decision, {'choose_b': random.choice([True, False])})

                    yield (pages.Belief_color, {'green_red': random.randint(0, 100)})
                    yield (pages.Belief_other, {'a_or_b': random.randint(0, 100)})

                    self.check_room_payoffs()

                    assert self.player.payoff == self.player.in_round(self.player.relevant_round).room_payoff

                    yield (pages.Results)