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

class Comprehension_2(Page):
    template_name = "zero_intro/Comprehension.html"
    form_model = "player"
    form_fields = ["c1_coplayer", "c2_probabilities", "c3_payoff_ab_red", "c4_payoff_ab_green", "c5_payoff_bb_green",
                   "c6_decision_importance"]

    def error_message(self, values):
        if self.player.treatment == 'human':
            c1_correct = 2
        else:
            c1_correct = 3

        if  values["c1_coplayer"] != c1_correct or \
            values["c2_probabilities"] != 1 or \
            values["c3_payoff_ab_red"] != 2 or \
            values["c4_payoff_ab_green"] != 1 or \
            values["c5_payoff_bb_green"] != 2 or \
            values["c6_decision_importance"] != 2:
            return "Please correct your answers."

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
