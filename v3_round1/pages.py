from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class DecisionInfo(Page):
    def is_displayed(self):
        return self.player.aa_treatment


class DecisionAssignment(Page):
    def is_displayed(self):
        return self.player.aa_treatment

    def before_next_page(self):
        self.player.action1_b = True


class Decision(Page):
    def is_displayed(self):
        return self.player.ra_treatment

    form_model = 'player'
    form_fields = ['action1_b']


class Belief_color(Page):
    form_model = 'player'
    form_fields = ['green_red']


class Belief_other(Page):
    form_model = 'player'
    form_fields = ['a_or_b']



page_sequence = [
    DecisionInfo,
    DecisionAssignment,
    Decision,
    Belief_color,
    Belief_other,
]
