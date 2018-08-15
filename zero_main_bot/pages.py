from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    template_name = "zero_shared/Decision.html"
    form_model = 'player'
    form_fields = ['choose_b']

    def before_next_page(self):
        self.player.draw_ball()
        self.player.get_coplayer_choice()
        self.player.calculate_round_payoff()
        if self.round_number == Constants.num_rounds:
            self.player.set_final_payoff()


class Belief_choice_chance_1(Page):
    template_name = "zero_shared/Belief_choice_chance.html"

    form_model = 'player'
    form_fields = ['choice_chance_1']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'second_time': False
        }

class Belief_color(Page):
    template_name = "zero_shared/Belief_color.html"
    form_model = 'player'
    form_fields = ['green_red']

class Belief_other(Page):
    template_name = "zero_shared/Belief_other.html"
    form_model = 'player'
    form_fields = ['a_or_b']


class Results(Page):
    template_name = "zero_shared/Results.html"
    def vars_for_template(self):
        return {
            'own_choice': "B" if self.player.choose_b else "A",
            'other_choice': "B" if self.player.other_choose_b else "A",
            'ball_color': "green" if self.player.ball_green else "red",
        }


class Belief_choice_chance_2(Page):
    template_name = "zero_shared/Belief_choice_chance.html"

    form_model = 'player'
    form_fields = ['choice_chance_2']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'second_time': True
        }

page_sequence = [
    Decision,
    Belief_choice_chance_1,
    Belief_color,
    Belief_other,
    Results,
    Belief_choice_chance_2,
]
