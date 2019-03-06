from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from otree_mturk_utils.views import CustomMturkPage


class Survey(CustomMturkPage):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'major', 'risk']

    def error_message(self, values):
        if values["education"] >= 2 and (values["major"] == " " or values["major"] is None):
            return "Please indicate your major."


class LastPage(CustomMturkPage):
    def vars_for_template(self):
        return {
            'payment_room': '1' if self.player.participant.vars.get('payment_room_1', None) else '2',
            'payment': self.player.participant.vars.get('payment', None),
            'experimenter_name': self.session.config.get('experimenter_name', 'Christian Koenig'),
            'experimenter_email': self.session.config.get('experimenter_email', 'christian.koenig@awi.uni-heidelberg.de')
        }

class Dropouts(Page):
    def is_displayed(self):
        return self.player.participant.vars.get('go_to_the_end', False)

    def vars_for_template(self):
        return {
            'experimenter_name': self.session.config.get('experimenter_name', 'Christian Koenig'),
            'experimenter_email': self.session.config.get('experimenter_email', 'christian.koenig@awi.uni-heidelberg.de')
        }

page_sequence = [
    Survey,
    LastPage,
    Dropouts
]
