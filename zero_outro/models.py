from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'zero_outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        verbose_name='What is your age?',
        min=13, max=125)

    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'I prefer not to tell'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect)

    education = models.StringField(
        choices=['Less than high school degree', 'High school degree or equivalent (e.g. GED)', 'Some college, but no degree', 'Associate degree',
                 'Bachelor degree', 'Graduate degree'],
        verbose_name='What is the highest level of school you have completed or the highest degree you have received?',
        widget=widgets.RadioSelect)

    major = models.StringField(
        verbose_name='If you had at least some college education, please tell us your major: ')

    risk = models.FloatField(
        min=0, max=10,
        verbose_name='How do you see yourself: Are you in general a person who takes risk (10) or do you try to avoid risks (0)? Please self-grade your choice (0-10).',
        widget=widgets.Slider(attrs={'step': '1'}, show_value=True), default=5,
    )