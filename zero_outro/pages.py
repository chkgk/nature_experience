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
            'payment_room': self.player.participant.vars.get('payment_room', None),
            'payment': self.player.participant.vars.get('payment', None),
            'experimenter_name': self.session.config.get('experimenter_name', 'Florian Diekert'),
            'experimenter_email': self.session.config.get('experimenter_email', 'natcoop@awi.uni-heidelberg.de')
        }


page_sequence = [
    Survey,
    LastPage
]
