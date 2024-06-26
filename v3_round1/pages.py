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
        self.player.set_participant_var()


class Decision(Page):
    def is_displayed(self):
        return self.player.ra_treatment

    form_model = 'player'
    form_fields = ['action1_b']

    def before_next_page(self):
        self.player.set_participant_var()


class Belief_color(Page):
    form_model = 'player'
    form_fields = ['green_red']


class Belief_other(Page):
    form_model = 'player'
    form_fields = ['a_or_b']


class FakeWait(Page):
    timeout_seconds = Constants.min_wait

    def is_displayed(self):
        return self.player.ra_treatment

    def vars_for_template(self):
        return {
            "title_text": "Please wait!"
        }


page_sequence = [
    DecisionInfo,
    DecisionAssignment,
    Decision,
    Belief_color,
    Belief_other,
    FakeWait,
]
