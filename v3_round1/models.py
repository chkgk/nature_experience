from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.conf import settings

author = 'Christian König gen. Kersting'

doc = """
Round 1 of Nature of Experience experiment
"""


class Constants(BaseConstants):
    name_in_url = 'v3_round1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.aa_treatment = player.participant.vars.get('aa_treatment', self.session.config.get('treatment') == 'AA')
            player.ra_treatment = player.participant.vars.get('ra_treatment', self.session.config.get('treatment') == 'RA')

            if settings.DEBUG:
                player.aa_treatment = self.session.config.get('treatment', 'AA') == 'AA'
                player.ra_treatment = self.session.config.get('treatment', 'RA') == 'RA'


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    aa_treatment = models.BooleanField(initial=False)
    ra_treatment = models.BooleanField(initial=False)

    action1_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        widget=widgets.RadioSelect(),
        verbose_name="Which action do you choose?",
        doc="whether the participant chose b or not")

    # beliefs
    green_red = models.IntegerField(min=0, max=100, doc="belief ball red / green")
    a_or_b = models.IntegerField(min=0, max=100, doc="belief choice other a / b")

    def set_participant_var(self):
        self.participant.vars["action1_b"] = self.action1_b