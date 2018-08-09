from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey(Page):
    form_model = 'player'
    form_fields = []

class LastPage(Page):
    def vars_for_template(self):
        return {
            'payoff_room': None,
            'room_pay': None,
        }

page_sequence = [
    Survey,
    LastPage
]
