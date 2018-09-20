from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)
import random

author = 'Christian König-Kersting'

doc = """
Human treatment of Nature of Experience project.
"""


class Constants(BaseConstants):
    name_in_url = 'zero_main_human'
    players_per_group = 2
    num_rounds = 2

    # parameters
    pi = 0.2
    ball_green_probability = 1 - pi

    prob_switch_a_to_b = 0.98
    prob_switch_b_to_a = 0.01

    # timeouts
    decision_timeout = 20 # 120s
    feelings_timeout = 60 # 60s

    # timeout banner is shown X seconds before timer runs out:
    time_left_warning = 30

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
            player.treatment = 'human'
            player.relevant_round = random.randint(1, 2)
            player.participant.vars['game_ended'] = False


class Group(BaseGroup):
    # chance
    ball_green = models.BooleanField(doc="whether the ball is green or red")

    # timeouts and dropouts
    dropout = models.BooleanField(initial=False, doc="whether or not a player has dropped out of the group")

    def draw_ball(self):
        self.ball_green = random.random() < Constants.ball_green_probability

    def get_coplayer_choices(self):
        for player in self.get_players():
            player.determine_implementation()
            player.get_coplayer_choice()

    def calculate_round_payoffs(self):
        for player in self.get_players():
            player.calculate_round_payoff()

    def set_final_payoffs(self):
        for player in self.get_players():
            player.set_final_payoff()


class Player(BasePlayer):
    # treatment
    treatment = models.CharField(choices=["computer", "human"], doc="treatment the participant played")

    # choices
    choose_b = models.BooleanField(
        choices=[(False, "A"), (True, "B")],
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="What do you choose?",
        doc="whether the participant chose b or not"
    )
    other_choose_b = models.BooleanField(doc="whether the co-player chose b or not")
    partner = models.PositiveSmallIntegerField(doc="id in subsession of matched player")

    # implementation
    implement_b = models.BooleanField(doc="whether b was actually implemented or not")

    # beliefs
    choice_chance_1 = models.IntegerField(min=0, max=100, doc="belief choice / chance before results")
    choice_chance_2 = models.IntegerField(min=0, max=100, doc="belief choice / chance after results")
    green_red = models.IntegerField(min=0, max=100, doc="belief ball red / green")
    a_or_b = models.IntegerField(min=0, max=100, doc="belief choice other a / b")

    # payoffs
    relevant_round = models.SmallIntegerField(min=1, max=Constants.num_rounds, doc="round selected for payment")
    room_payoff = models.CurrencyField(doc="payoff earned in this room if selected for payment")

    # timeouts / dropouts
    timeout_decision = models.BooleanField(initial=False, doc="whether player timed out making a decision")
    timeout_feelings = models.BooleanField(initial=False, doc="whether player timed out answering the feelings questions")

    # methods
    def determine_implementation(self):
        if self.round_number == 1:
            random_number = random.random()
            if self.choose_b:
                self.implement_b = random_number >= Constants.prob_switch_b_to_a
            else:
                # a chosen
                self.implement_b = random_number < Constants.prob_switch_a_to_b
        else:
            # in round two, choices are directly implemented.
            self.implement_b = self.choose_b

    def set_partner(self):
        self.partner = self.get_others_in_group()[0].id_in_subsession

    def get_coplayer_choice(self):
        others = self.get_others_in_group()
        if others:
            self.other_choose_b = others[0].choose_b

    def calculate_round_payoff(self):
        if self.other_choose_b is not None:
            if self.group.ball_green:
                self.room_payoff = c(Constants.payoff_matrix[self.implement_b][self.other_choose_b])
            else:
                self.room_payoff = c(0)
        else:
            self.room_payoff = c(0)

    def set_final_payoff(self):
        self.payoff = self.in_round(self.relevant_round).room_payoff
        self.participant.vars['payment'] = self.payoff
        self.participant.vars['payment_room'] = self.relevant_round

    def end_game(self):
        self.participant.vars['go_to_the_end'] = True
        # self.participant.vars['game_ended'] = True