from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):

        comprehension_inputs = {
            "c1_coplayer": 2 if self.player.treatment == "human" else 3,
            "c2_probabilities": 1,
            "c3_payoff_ab_red": 2,
            "c4_payoff_ab_green": 1,
            "c5_payoff_bb_green": 2,
            "c6_decision_importance": 2
        }

        yield (pages.Introduction)
        if self.player.treatment == 'human':
            assert "co-player is another participant" in self.html
            assert "co-player chooses A" in self.html
        else:
            assert "co-player is not a human" in self.html
            assert "computer chooses A" in self.html

        yield (pages.Rules)

        yield (pages.Comprehension_1, comprehension_inputs)

        yield SubmissionMustFail(pages.Comprehension_2, {})
        yield (pages.Comprehension_2, comprehension_inputs)
