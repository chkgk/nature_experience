from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Christian König gen. Kersting'

doc = """
Grouping and results after round 1
"""


class Constants(BaseConstants):
    name_in_url = 'v3_results_2'
    players_per_group = 2
    num_rounds = 1

    ball_green_probability = 0.4 # double check

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
    pass


class Group(BaseGroup):
    ball_green = models.BooleanField()

    def draw_ball(self):
        self.ball_green = random.random() < Constants.ball_green_probability

class Player(BasePlayer):
    action = models.BooleanField()
    others_action = models.BooleanField()
    former_partner_id_in_subsession = models.IntegerField()
    partner_id_in_subsession = models.IntegerField()
    room_payoff = models.CurrencyField()

    def set_partner_action(self):
        self.action = self.participant.vars.get("action2_b", False)
        self.former_partner_id_in_subsession = self.participant.vars.get('partner_1')

        partner = self.get_others_in_group()[0]
        self.partner_id_in_subsession = partner.id_in_subsession

        self.others_action = partner.participant.vars.get('action2_b')
        self.participant.vars["partner_2"] = self.partner_id_in_subsession

    def calculate_round_payoff(self):
        if self.others_action is not None:
            if self.group.ball_green:
                self.room_payoff = c(Constants.payoff_matrix[self.action][self.others_action])
            else:
                self.room_payoff = c(0)
        else:
            self.room_payoff = c(0)

        self.participant.vars["ball_green_2"] = self.group.ball_green
        self.participant.vars["room_payoff_2"] = self.room_payoff

        if not self.participant.vars.get('payment_room_1'):
            self.participant.vars["payment"] = self.room_payoff
            self.payoff = self.room_payoff