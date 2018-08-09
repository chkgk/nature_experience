from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian König-Kersting'

doc = """
Computer treatment of Nature of Experience project.
"""


class Constants(BaseConstants):
    name_in_url = 'zero_main_bot'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.treatment = self.session.config.get('treatment', 'computer')


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.CharField(choices=["computer", "human"], doc="treatment the participant played")
