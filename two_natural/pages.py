from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Instructions1(Page):
    pass

class Comprehension1(Page):
    template_name = "two_natural/Comprehension1.html"
    form_model = "player"
    form_fields = ["c1_coplayer", "c2_probabilities", "c3_decision_importance"]

    def vars_for_template(self):
        return {
            'page': 1,
            'c1_ok': False,
            'c2_ok': False,
            'c3_ok': False,
        }

class Comprehension1_check(Page):
    template_name = "two_natural/Comprehension1.html"
    form_model = "player"
    form_fields = ["c1_coplayer", "c2_probabilities", "c3_decision_importance"]

    def vars_for_template(self):
        return {
            'page': 2,
            'c1_ok': self.player.c1_coplayer == Constants.comprehension_solutions["c1_coplayer"],
            'c2_ok': self.player.c2_probabilities == Constants.comprehension_solutions["c2_probabilities"],
            'c3_ok': self.player.c3_decision_importance == Constants.comprehension_solutions["c3_decision_importance"],
        }

    def error_message(self, values):
        if values["c1_coplayer"] != Constants.comprehension_solutions["c1_coplayer"] or \
           values["c2_probabilities"] != Constants.comprehension_solutions["c2_probabilities"] or \
           values["c3_decision_importance"] != Constants.comprehension_solutions["c3_decision_importance"]:
            return "Please check your answers again!"

class Comprehension2(Page):
    template_name = "two_natural/Comprehension2.html"
    form_model = "player"
    form_fields = ["c4_payoff_ab_red", "c5_payoff_ab_green", "c6_payoff_bb_green", "c7_payoff_ba_green"]

    def vars_for_template(self):
        return {
            'page': 1,
            'c4_ok': False,
            'c5_ok': False,
            'c6_ok': False,
            'c7_ok': False,
        }

class Comprehension2_check(Page):
    template_name = "two_natural/Comprehension2.html"
    form_model = "player"
    form_fields = ["c4_payoff_ab_red", "c5_payoff_ab_green", "c6_payoff_bb_green", "c7_payoff_ba_green"]

    def vars_for_template(self):
        return {
            'page': 2,
            'c4_ok': self.player.c4_payoff_ab_red == Constants.comprehension_solutions["c4_payoff_ab_red"],
            'c5_ok': self.player.c5_payoff_ab_green == Constants.comprehension_solutions["c5_payoff_ab_green"],
            'c6_ok': self.player.c6_payoff_bb_green == Constants.comprehension_solutions["c6_payoff_bb_green"],
            'c7_ok': self.player.c7_payoff_ba_green == Constants.comprehension_solutions["c7_payoff_ba_green"],
        }

    def error_message(self, values):
        if values["c4_payoff_ab_red"] != Constants.comprehension_solutions["c4_payoff_ab_red"] or \
           values["c5_payoff_ab_green"] != Constants.comprehension_solutions["c5_payoff_ab_green"] or \
           values["c6_payoff_bb_green"] != Constants.comprehension_solutions["c6_payoff_bb_green"] or \
           values["c7_payoff_ba_green"] != Constants.comprehension_solutions["c7_payoff_ba_green"]:
            return "Please check your answers again!"

class ActionPreference(Page):
    def is_displayed(self):
        return self.player.aa_treatment

    form_model = 'player'
    form_fields = ["prefers_b"]


class DecisionInfo(Page):
    def is_displayed(self):
        return self.player.aa_treatment

class DecisionAssignment(Page):
    def is_displayed(self):
        return self.player.aa_treatment

    def before_next_page(self):
        self.player.action1_b = True
        self.player.set_participant_var()

class Decision1(Page):
    def is_displayed(self):
        return self.player.ra_treatment

    form_model = 'player'
    form_fields = ['action1_b']

    def before_next_page(self):
        self.player.set_participant_var()


class Belief_color1(Page):
    form_model = 'player'
    form_fields = ['green_red_r1']


class Belief_other1(Page):
    form_model = 'player'
    form_fields = ['a_or_b_r1']


class Match1(Page):
    timeout_seconds = Constants.min_wait

    def vars_for_template(self):
        return {
            "title_text": "Please wait!"
        }

    def before_next_page(self):
        self.player.draw_ball_r1()
        self.player.draw_action_r1()
        self.player.calculate_payoff_r1()


class Decision2(Page):
    form_model = 'player'
    form_fields = ['action2_b']

    def before_next_page(self):
        self.player.determine_switch()

class Belief_color2(Page):
    form_model = 'player'
    form_fields = ['green_red_r2']


class Belief_other2(Page):
    form_model = 'player'
    form_fields = ['a_or_b_r2']

class Motivation(Page):
    form_model = 'player'
    form_fields = ['motivation', 'motivation_other']

    def vars_for_template(self):
        return {
            'first_round_action': 'B' if self.player.action1_b else 'A',
            'current_action': 'B' if self.player.action2_b else 'A',
        }

    def error_message(self, values):
        if values["motivation"] == 6 and (values["motivation_other"] is None or values["motivation_other"].strip() == ""):
            return "Please specify your motivation."

class Match2(Page):
    timeout_seconds = Constants.min_wait

    def vars_for_template(self):
        return {
            "title_text": "Please wait!"
        }

    def before_next_page(self):
        self.player.draw_ball_r2()
        self.player.draw_action_r2()
        self.player.calculate_payoff_r2()

class Results1(Page):
    def vars_for_template(self):
        return {
            'own_action': 'B' if self.player.action1_b else 'A',
            'others_action': 'B' if self.player.other_b_r1 else 'A',
            'ball_color': 'green' if self.player.ball_green_r1 else 'red',
        }

class Results2(Page):
    def vars_for_template(self):
        return {
            'own_action': 'B' if self.player.action2_b else 'A',
            'others_action': 'B' if self.player.other_b_r2 else 'A',
            'ball_color': 'green' if self.player.ball_green_r2 else 'red',
        }
    
class Survey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'major', 'risk']

    def error_message(self, values):
        if values["education"] >= 2 and (values["major"] == " " or values["major"] is None):
            return "Please indicate your major."


class LastPage(Page):
    def vars_for_template(self):
        return {
            'payment_room': '1' if self.player.participant.vars.get('payment_room_1', None) else '2',
            'payment': self.player.participant.vars.get('payment', None),
            'experimenter_name': self.session.config.get('experimenter_name', 'Christian Koenig'),
            'experimenter_email': self.session.config.get('experimenter_email', 'christian.koenig@uibk.ac.at')
        }


page_sequence = [
    Introduction,
    Instructions1,
    Comprehension1,
    Comprehension1_check,
    Comprehension2,
    Comprehension2_check,
    ActionPreference,
    DecisionInfo,
    DecisionAssignment,
    Decision1,
    Belief_color1,
    Belief_other1,
    Match1,
    Results1,
    Decision2,
    Belief_color2,
    Belief_other2,
    Motivation,
    Match2,
    Results2,
    Survey,
    LastPage
]