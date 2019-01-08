from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ActionPreference(Page):
    def is_displayed(self):
        return self.player.aa_treatment

    form_model = 'player'
    form_fields = ["prefers_B"]

page_sequence = [
    ActionPreference
]
