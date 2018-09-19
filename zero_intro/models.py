from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian König-Kersting'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'zero_intro'
    players_per_group = None
    num_rounds = 1

    comprehension_solutions = {
        "c1_coplayer": {
            'human': 2,
            'computer': 3
        },
        "c2_probabilities": 1,
        "c3_payoff_ab_red": 2,
        "c4_payoff_ab_green": 1,
        "c5_payoff_bb_green": 2,
        "c6_decision_importance": 2,
    }

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.treatment = self.session.config.get('treatment', 'computer')


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.CharField(choices=["computer", "human"], doc="treatment the participant played")

    c1_coplayer = models.SmallIntegerField(
        choices=[[1, 'the same real person in both rooms.'],
                 [2, 'a different real person in each room.'],
                 [3, 'a computer player.']],
        verbose_name='Which of the following is correct? In Room 2 and 3, my co-player is',
        widget=widgets.RadioSelect)

    c2_probabilities = models.SmallIntegerField(
        choices=[[1, 'choose A more often than B.'],
                 [2, 'choose B more often than A.'],
                 [3, 'choose A and B equally often.']],
        verbose_name='Which of the following is correct? On average, co-players',
        widget=widgets.RadioSelect)

    c3_payoff_ab_red = models.SmallIntegerField(
        choices=[[1, 'US$ 1'],
                 [2, 'US$ 0'],
                 [3, 'US$ 3']],
        verbose_name="What is your payout if action A is implemented for you, your co-player's action is B, and the ball is red?",
        widget=widgets.RadioSelect)

    c4_payoff_ab_green = models.SmallIntegerField(
        choices=[[1, 'US $ 1'],
                 [2, 'US $ 0'],
                 [3, 'US $ 3']],
        verbose_name="What is your payout if action A is implemented for you, your co-player's action is B, and the ball is green?",
        widget=widgets.RadioSelect)

    c5_payoff_bb_green = models.SmallIntegerField(
        choices=[[1, 'US $ 1'],
                 [2, 'US $ 0'],
                 [3, 'US $ 3']],
        verbose_name="What is your payout if action B is implemented for you, your co-player's action is B, and the ball is green?",
        widget=widgets.RadioSelect)


    c6_decision_importance = models.SmallIntegerField(
        choices=[[1, 'The second decision is less important than the first one.'],
                 [2, 'Both decisions are equally important.'],
                 [3, 'The second decision is more important than the first one.']],
        verbose_name='Remember that only one of the two choices counts for your payment, with equal chance. What does this mean?',
        widget=widgets.RadioSelect)
