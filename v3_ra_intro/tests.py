from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):

        comprehension1 = {
            "c1_coplayer": Constants.comprehension_solutions["c1_coplayer"],
            "c2_probabilities": Constants.comprehension_solutions["c2_probabilities"],
            "c3_decision_importance": Constants.comprehension_solutions["c3_decision_importance"],
        }

        comprehension2 = {
            "c4_payoff_ab_red": Constants.comprehension_solutions["c4_payoff_ab_red"],
            "c5_payoff_ab_green": Constants.comprehension_solutions["c5_payoff_ab_green"],
            "c6_payoff_bb_green": Constants.comprehension_solutions["c6_payoff_bb_green"],
            "c7_payoff_ba_green": Constants.comprehension_solutions["c7_payoff_ba_green"],
        }


        yield (pages.Introduction)
        yield (pages.Instructions1)
        yield (pages.Comprehension1, comprehension1)
        yield (pages.Comprehension1_check, comprehension1)
        yield (pages.Comprehension2, comprehension2)
        yield (pages.Comprehension2_check, comprehension2)

        if self.player.aa_treatment:
            yield (pages.ActionPreference, {"prefers_B": random.choice([True, False])})
