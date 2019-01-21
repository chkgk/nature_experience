from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Decision(Page):
    form_model = 'player'
    form_fields = ['action2_b']

    def before_next_page(self):
        self.player.determine_switch()

class Belief_color(Page):
    form_model = 'player'
    form_fields = ['green_red']


class Belief_other(Page):
    form_model = 'player'
    form_fields = ['a_or_b']

class Motivation(Page):
    form_model = 'player'
    form_fields = ['motivation', 'motivation_other']

    def vars_for_template(self):
        return {
            'first_round_action': 'B' if self.player.action1_b else 'A',
            'current_action': 'B' if self.player.action2_b else 'A',
        }

    def error_message(self, values):
        if values["motivation"] == 6 and (values["motivation_other"] is None or values["motivation_other"].strip() == ""):
            return "Please specify your motivation."

page_sequence = [
    Decision,
    Belief_color,
    Belief_other,
    Motivation,
]
