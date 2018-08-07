from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'zero_intro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    question1 = models.IntegerField(
        choices=[[0, 'the same real person in both rooms.'],
                 [2, 'a different real person in each room.'],
                 [1, 'a computer player.']],
        verbose_name='Which of the following is correct? In Room 2 and 3, my co-player is',
        widget=widgets.RadioSelect)

    ##If human: option 2 is correct; else if robot: option 3 is correct##

    ### questionx2 occurs if questionx is answered incorrectly. ###
    ### values 0 and 1 are always wrong, value 2 is the correct answer ###

    question2 = models.IntegerField(
        choices=[[0, 'choose A more often than B.'],
                 [2, 'choose B more often than A.'],
                 [1, 'choose A and B equally often.']],
        verbose_name='Which of the following is correct? On average, co-players',
        widget=widgets.RadioSelect)

    ## [option 1 is correct]  ##

    question3 = models.IntegerField(
        choices=[[2, 'US$ 1'],
                 [1, 'US$ 0'],
                 [0, 'US$ 3']],
        verbose_name='What is your payout if you choose A, your co-player chooses B, and the ball is red?',
        widget=widgets.RadioSelect)

    ## [option 2 is correct] ##

    question4 = models.IntegerField(
        choices=[[0, 'US $ 1'],
                 [2, 'US $ 0'],
                 [1, 'US $ 3']],
        verbose_name='What is your payout if you choose A, your co-player chooses B, and the ball is green?',
        widget=widgets.RadioSelect)

    ##[option 1 is correct]  ##

    question5 = models.IntegerField(
        choices=[[0, 'US $ 1'],
                 [2, 'US $ 0'],
                 [1, 'US $ 3']],
        verbose_name='What is your payout if you choose B, your co-player chooses B, and the ball is green? ',
        widget=widgets.RadioSelect)

    ## [option 2 is correct] ##

    question6 = models.IntegerField(
        choices=[[0, 'The second decision is less important than the first one.'],
                 [2, 'Both decisions are equally important.'],
                 [1, 'The second decision is more important than the first one.']],
        verbose_name='Remember that only one of the two choices counts for your payment, with equal chance. What does this mean?',
        widget=widgets.RadioSelect)

    ## [option 2 is correct] ##
