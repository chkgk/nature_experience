from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class LastPage (Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Survey (Page):
    pass


page_sequence = [
    Survey,
    LastPage
]
