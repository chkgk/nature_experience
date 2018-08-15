from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Christian König-Kersting'

doc = """
Computer treatment of Nature of Experience project.
"""


class Constants(BaseConstants):
    name_in_url = 'zero_main_bot'
    players_per_group = None
    num_rounds = 2

    pi = 0.2
    computer_b_probability = 0.4
    ball_green_probability = 1 - pi

    # note: False = red, True = green
    payoff_matrix = {
        False:
            {
                False: 1,
                True: 1
            },
        True:
            {
                False: 3,
                True: 0
            }
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.treatment = self.session.config.get('treatment', 'computer')
            player.relevant_round = random.randint(1, 2)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # treatment
    treatment = models.CharField(choices=["computer", "human"], doc="treatment the participant played")

    # chance
    ball_green = models.BooleanField(doc="whether the ball is green or red")

    # choices
    choose_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="What do you choose?",
        doc="whether the participant chose b or not"
    )
    other_choose_b = models.BooleanField(doc="whether the co-player chose b or not")

    # beliefs
    choice_chance_1 = models.IntegerField(min=0, max=100, doc="belief choice / chance before results")
    choice_chance_2 = models.IntegerField(min=0, max=100, doc="belief choice / chance after results")
    green_red = models.IntegerField(min=0, max=100, doc="belief ball red / green")
    a_or_b = models.IntegerField(min=0, max=100, doc="belief choice other a / b")

    # payoffs
    relevant_round = models.SmallIntegerField(min=1, max=Constants.num_rounds, doc="round selected for payment")
    room_payoff = models.CurrencyField(doc="payoff earned in this room if selected for payment")

    # methods
    def get_coplayer_choice(self):
        self.other_choose_b = random.random() <= Constants.computer_b_probability

    def draw_ball(self):
        self.ball_green = random.random() <= Constants.ball_green_probability

    def calculate_round_payoff(self):
        if self.ball_green:
            self.room_payoff = c(Constants.payoff_matrix[self.choose_b][self.other_choose_b])
        else:
            self.room_payoff = c(0)

    def set_final_payoff(self):
        self.payoff = self.in_round(self.relevant_round).room_payoff
        self.participant.vars['payment'] = self.payoff
        self.participant.vars['payment_room'] = self.relevant_round