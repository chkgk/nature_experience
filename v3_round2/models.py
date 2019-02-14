from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.conf import settings
import random

author = 'Christian König gen. Kersting'

doc = """
Round 2 app of Nature of Experience Project
"""


class Constants(BaseConstants):
    name_in_url = 'v3_round2'
    players_per_group = None
    num_rounds = 1

    min_wait = 5

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.aa_treatment = player.participant.vars.get('aa_treatment', self.session.config.get('treatment') == 'AA')
            player.ra_treatment = player.participant.vars.get('ra_treatment', self.session.config.get('treatment') == 'RA')
            player.action1_b = player.participant.vars.get('action1_b', False)

            if settings.DEBUG:
                player.aa_treatment = self.session.config.get('treatment', 'AA') == 'AA'
                player.ra_treatment = self.session.config.get('treatment', 'RA') == 'RA'
                player.action1_b = random.choice([True, False])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    aa_treatment = models.BooleanField(initial=False)
    ra_treatment = models.BooleanField(initial=False)

    action1_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        doc="whehter the participant chose b in round 1")

    action2_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        widget=widgets.RadioSelect(),
        verbose_name="Which action do you choose?",
        doc="whether the participant chose b in round 2")

    switcher = models.BooleanField(
        doc="whether or not the participant switched actions between rounds")

    # beliefs
    green_red = models.IntegerField(min=0, max=100, doc="belief ball red / green")
    a_or_b = models.IntegerField(min=0, max=100, doc="belief choice other a / b")

    # motivations for action choice in secound round
    motivation = models.IntegerField(min=1, max=6)
    motivation_other = models.CharField(blank=True)

    def determine_switch(self):
        self.switcher = self.action1_b != self.action2_b
        self.participant.vars["action2_b"] = self.action2_b
        self.participant.vars["switcher"] = self.switcher