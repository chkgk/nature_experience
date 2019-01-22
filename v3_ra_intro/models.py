from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Christian König-Kersting'

doc = """
V3 of Nature of Experience Project
"""


class Constants(BaseConstants):
    name_in_url = 'v3_ra_intro'
    players_per_group = None
    num_rounds = 1

    comprehension_solutions = {
        'c1_coplayer': 2,
        'c2_probabilities': 1,
        'c3_decision_importance': 2,
        'c4_payoff_ab_red': 1,
        'c5_payoff_ab_green': 2,
        'c6_payoff_bb_green': 1,
        'c7_payoff_ba_green': 3 
    }

class Subsession(BaseSubsession):
    def creating_session(self):
        treatment = self.session.config.get('treatment')
        aa_treatment = treatment == 'AA'
        ra_treatment = treatment == 'RA'

        for player in self.get_players():
            player.aa_treatment = aa_treatment
            player.ra_treatment = ra_treatment
            player.payment_room_1 = random.choice([True, False])

            player.participant.vars["aa_treatment"] = aa_treatment
            player.participant.vars["ra_treatment"] = ra_treatment
            player.participant.vars["payment_room_1"] = player.payment_room_1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    aa_treatment = models.BooleanField(initial=False)
    ra_treatment = models.BooleanField(initial=False)

    payment_room_1 = models.BooleanField(doc="True if room 1 is paid, False if room 2 is paid.")
    
    c1_coplayer = models.SmallIntegerField(
        choices=[[1, 'the same participant in both rounds.'],
                 [2, 'a different participant in each round.']],
        verbose_name='1. Which of the following is correct? In the first round and in the second round, my co-player is',
        widget=widgets.RadioSelect)

    c2_probabilities = models.SmallIntegerField(
        choices=[[1, 'choose A more often than B.'],
                 [2, 'choose B more often than A.'],
                 [3, 'choose A and B equally often.']],
        verbose_name='2. Which of the following is correct? On average, co-players',
        widget=widgets.RadioSelect)

    c3_decision_importance = models.SmallIntegerField(
        choices=[[1, 'The outcome of round 1 is less important than the outcome of round 2.'],
                 [2, 'The outcomes of both rounds are equally important.'],
                 [3, 'The outcome of round 2 is less important than the outcome of round 1.']],
        verbose_name='3. Remember that only one of the two rounds counts for your payment, with equal chance. What does this mean?',
        widget=widgets.RadioSelect)

    c4_payoff_ab_red = models.SmallIntegerField(
        choices=[[1, 'US$ 0'],
                 [2, 'US$ 1'],
                 [3, 'US$ 3']],
        verbose_name="4. What is your payout if your action is A, your co-player’s action is B, and the ball is red?",
        widget=widgets.RadioSelect)

    c5_payoff_ab_green = models.SmallIntegerField(
        choices=[[1, 'US $ 0'],
                 [2, 'US $ 1'],
                 [3, 'US $ 3']],
        verbose_name="5. What is your payout if your action is A, your co-player’s action is B, and the ball is green?",
        widget=widgets.RadioSelect)

    c6_payoff_bb_green = models.SmallIntegerField(
        choices=[[1, 'US $ 0'],
                 [2, 'US $ 1'],
                 [3, 'US $ 3']],
        verbose_name="6. What is your payout if your action is B, your co-player’s action is B, and the ball is green?",
        widget=widgets.RadioSelect)

    c7_payoff_ba_green = models.SmallIntegerField(
        choices=[[1, 'US $ 0'],
                 [2, 'US $ 1'],
                 [3, 'US $ 3']],
        verbose_name="7. What is your payout if your action is B, your co-player’s action is A, and the ball is green?",
        widget=widgets.RadioSelect)

    prefers_B = models.BooleanField(
        choices=[(False, 'Option A'), (True, 'Option B')],
        verbose_name="A final question, for which there is no right or wrong answer: Which action would you choose?",
        blank=True,
        widget=widgets.RadioSelect)
