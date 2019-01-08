from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'v3_aa'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.aa_treatment = True
            player.ra_treatment = False


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    aa_treatment = models.BooleanField(initial=False)
    ra_treatment = models.BooleanField(initial=False)
