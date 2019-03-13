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

            if settings.DEBUG:
                player.aa_treatment = self.session.config.get('treatment', 'AA') == 'AA'
                player.ra_treatment = self.session.config.get('treatment', 'RA') == 'RA'
                player.action1_b = random.choice([True, False])


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    aa_treatment = models.BooleanField(initial=False, doc="True (1) if AA treatment, else False (0)")
    ra_treatment = models.BooleanField(initial=False, doc="True (1) if AA treatment, else False (0)")

    action1_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        doc="Round 1, True (1) if participant chose B, else False (0).")

    action2_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        widget=widgets.RadioSelect(),
        verbose_name="Which action do you choose?",
        doc="Round 2, True (1) if participant chose B, else False (0).")

    switcher = models.BooleanField(
        doc="True (1) if participant switched actions (A/B) between rounds.")

    # beliefs
    green_red = models.IntegerField(min=0, max=100, doc="Round 1, Belief about ball being red or green.")
    a_or_b = models.IntegerField(min=0, max=100, doc="Round 1, Belief about others' action being A or B")

    # motivations for action choice in secound round
    motivation = models.IntegerField(min=1, max=6, doc="Motivation selected for switching, respectively sticking to the same action.")
    motivation_other = models.CharField(blank=True, doc="Free text input for other motivations if motivation == 6")

    def determine_switch(self):
        self.action1_b = self.participant.vars.get('action1_b', False)
        self.switcher = self.action1_b != self.action2_b
        self.participant.vars["action2_b"] = self.action2_b
        self.participant.vars["switcher"] = self.switcher