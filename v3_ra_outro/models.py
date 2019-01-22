from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian König gen. Kersting'

doc = """
Survey for nature of experience project
"""


class Constants(BaseConstants):
    name_in_url = 'v3_ra_outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # survey
    age = models.IntegerField(
        verbose_name='What is your age?',
        min=13, max=125
    )

    gender = models.StringField(
        choices=['Male', 'Female', 'Other', 'I prefer not to tell'],
        verbose_name='What is your gender?',
        widget=widgets.RadioSelect
    )

    education = models.IntegerField(
        choices=[
            (0, 'Less than high school degree'),
            (1, 'High school degree or equivalent (e.g. GED)'),
            (2, 'Some college, but no degree'),
            (3, 'Associate degree'),
            (4, 'Bachelor degree'),
            (5, 'Graduate degree')
        ],
        verbose_name='What is the highest level of school you have completed or the highest degree you have received?',
        widget=widgets.RadioSelect)

    major = models.StringField(
        verbose_name='If you had at least some college education, please tell us your major: ',
        blank=True
    )

    risk = models.FloatField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        verbose_name='How do you see yourself: Are you in general a person who takes risk (10) or do you try to avoid \
                risks (0)? Please self-grade your choice (0-10).',
        widget=widgets.RadioSelectHorizontal(),
    )
