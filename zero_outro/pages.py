from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'major', 'risk']

    def error_message(self, values):
        if values["education"] >= 2 and (values["major"] == "" or values["major"] == None):
            return "Please indicate your major."

class LastPage(Page):
    def vars_for_template(self):
        return {
            'payoff_room': None,
            'room_pay': None,
            'experimenter_name': self.session.config.get('experimenter_name', 'Florian Diekert'),
            'experimenter_email': self.session.config.get('experimenter_email', 'natcoop@awi.uni-heidelberg.de')
        }


page_sequence = [
    Survey,
    LastPage
]
