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
    name_in_url = 'v3_results_1'
    players_per_group = 2
    num_rounds = 1

    ball_green_probability = 0.8 # double check

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
    ball_green = models.BooleanField(doc="True (1) if color of ball drawn is green in round 1, else False (0).")

    def draw_ball(self):
        self.ball_green = random.random() < Constants.ball_green_probability

class Player(BasePlayer):
    action = models.BooleanField(doc="True (1) if B was played in round 1, else False (0).")
    others_action = models.BooleanField(doc="True (1) if co-player played B in round 1, else False (0).")
    partner_id_in_subsession = models.IntegerField(doc="Round 1, Co-player's ID (in subsession)")
    room_payoff = models.CurrencyField(doc="Payoff for room 1, if selected for payment.")

    def set_partner_action(self):
        self.action = self.participant.vars.get('action1_b')

        partner = self.get_others_in_group()[0]
        self.partner_id_in_subsession = partner.id_in_subsession
        self.others_action = partner.participant.vars.get('action1_b')
        self.participant.vars["partner_1"] = self.partner_id_in_subsession

    def calculate_round_payoff(self):
        if self.others_action is not None:
            if self.group.ball_green:
                self.room_payoff = c(Constants.payoff_matrix[self.action][self.others_action])
            else:
                self.room_payoff = c(0)
        else:
            self.room_payoff = c(0)

        self.participant.vars["ball_green_1"] = self.group.ball_green
        self.participant.vars["room_payoff_1"] = self.room_payoff

