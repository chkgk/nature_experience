from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction (Page):
    pass

class Rules (Page):
    pass

class Comprehension_1(Page):
    template_name = "zero_intro/Comprehension.html"
    form_model = "player"
    form_fields = ["c1_coplayer", "c2_probabilities", "c3_payoff_ab_red", "c4_payoff_ab_green", "c5_payoff_bb_green", "c6_decision_importance"]

    def vars_for_template(self):
        return {
            'page': 1,
            'c1_ok': False,
            'c2_ok': False,
            'c3_ok': False,
            'c4_ok': False,
            'c5_ok': False,
            'c6_ok': False
        }

class Comprehension_2(Page):
    template_name = "zero_intro/Comprehension.html"
    form_model = "player"
    form_fields = ["c1_coplayer", "c2_probabilities", "c3_payoff_ab_red", "c4_payoff_ab_green", "c5_payoff_bb_green",
                   "c6_decision_importance"]

    def vars_for_template(self):
        return {
            'page': 2,
            'c1_ok': self.player.c1_coplayer == Constants.comprehension_solutions["c1_coplayer"][self.player.treatment],
            'c2_ok': self.player.c2_probabilities == Constants.comprehension_solutions["c2_probabilities"],
            'c3_ok': self.player.c3_payoff_ab_red == Constants.comprehension_solutions["c3_payoff_ab_red"],
            'c4_ok': self.player.c4_payoff_ab_green == Constants.comprehension_solutions["c4_payoff_ab_green"],
            'c5_ok': self.player.c5_payoff_bb_green == Constants.comprehension_solutions["c5_payoff_bb_green"],
            'c6_ok': self.player.c6_decision_importance == Constants.comprehension_solutions["c6_decision_importance"]
        }

    def error_message(self, values):
        if values["c1_coplayer"] != Constants.comprehension_solutions["c1_coplayer"][self.player.treatment] or \
            values["c2_probabilities"] != Constants.comprehension_solutions["c2_probabilities"] or \
            values["c3_payoff_ab_red"] != Constants.comprehension_solutions["c3_payoff_ab_red"] or \
            values["c4_payoff_ab_green"] != Constants.comprehension_solutions["c4_payoff_ab_green"] or \
            values["c5_payoff_bb_green"] != Constants.comprehension_solutions["c5_payoff_bb_green"] or \
            values["c6_decision_importance"] != Constants.comprehension_solutions["c6_decision_importance"]:
            return "Please check your answers again!"



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Rules,
    Comprehension_1,
    Comprehension_2
]
