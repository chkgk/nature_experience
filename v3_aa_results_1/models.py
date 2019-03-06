from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import csv


author = 'Christian König gen. Kersting'

doc = """
Round 1 results for AA treatment.
"""


class Constants(BaseConstants):
    name_in_url = 'v3_aa_results_1'
    players_per_group = None
    num_rounds = 1

    ball_green_probability = 0.4  # double check

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

    data_file = "__temp_bots_Mar06_15h23m51.1s/v3_round1.csv"
    min_wait = 5
    max_wait = 20

class Subsession(BaseSubsession):
    b_observations = models.IntegerField()
    a_observations = models.IntegerField()
    b_proportion = models.FloatField()

    def creating_session(self):
        a_counter = 0
        b_counter = 0
        with open(Constants.data_file, 'r') as csv_file:
            ra_data = csv.DictReader(csv_file)
            for row in ra_data:
                if row["player.action1_b"] == '1':
                    b_counter += 1
                elif row["player.action1_b"] == '0':
                    a_counter += 1

        if (a_counter + b_counter) == 0:
            raise Exception('No data found.')

        self.a_observations = a_counter
        self.b_observations = b_counter
        self.b_proportion = b_counter / (b_counter + a_counter)

        for player in self.get_players():
            player.set_timeout()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    action = models.BooleanField()
    others_action = models.BooleanField()
    room_payoff = models.CurrencyField()

    ball_green = models.BooleanField()
    matching_timeout = models.IntegerField()

    def set_timeout(self):
        self.matching_timeout = random.randint(Constants.min_wait, Constants.max_wait)

    def draw_ball(self):
        self.ball_green = random.random() < Constants.ball_green_probability

    def set_partner_action(self):
        self.action = self.participant.vars.get('action1_b', False)

        # determine partner action here
        self.others_action = random.random() <= self.subsession.b_proportion

    def calculate_round_payoff(self):
        if self.others_action is not None:
            if self.ball_green:
                self.room_payoff = c(Constants.payoff_matrix[self.action][self.others_action])
            else:
                self.room_payoff = c(0)
        else:
            self.room_payoff = c(0)

        self.participant.vars["ball_green_1"] = self.ball_green
        self.participant.vars["room_payoff_1"] = self.room_payoff

        if self.participant.vars.get('payment_room_1'):
            self.participant.vars["payment"] = self.room_payoff
            self.payoff = self.room_payoff
