from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Decision(Page):
    form_model = 'player'
    form_fields = ['action2_b']


class Belief_color(Page):
    form_model = 'player'
    form_fields = ['green_red']


class Belief_other(Page):
    form_model = 'player'
    form_fields = ['a_or_b']

class Motivation(Page):
    def vars_for_template(self):
        # fix changer indicator
        return {
            'changer': True,
            'first_round_action': 'A',
            'current_action': 'B' if self.player.action2_b else 'A',
        }

page_sequence = [
    Decision,
    #Belief_color,
    #Belief_other,
    Motivation,
]
