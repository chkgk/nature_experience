from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    pass

class Belief_choice_chance_1(Page):
    template_name = "zero_main_bot/Belief_choice_chance.html"

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'second_time': False
        }

class Belief_color(Page):
    pass

class Belief_other(Page):
    pass

class Belief_choice_chance_2(Page):
    template_name = "zero_main_bot/Belief_choice_chance.html"

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'second_time': True
        }

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass

class Results(Page):
    pass


page_sequence = [
    Decision,
    Belief_choice_chance_1,
    Belief_color,
    Belief_other,
    ResultsWaitPage,
    Results,
    Belief_choice_chance_2,
]
