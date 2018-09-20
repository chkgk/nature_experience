from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage
from .models import Constants

class GroupWaitPage(CustomMturkWaitPage):
    template_name = "zero_main_human/GroupingWaitPage.html"
    group_by_arrival_time = True
    startwp_timer = 10 # 120
    skip_until_the_end_of = 'experiment'

    def is_displayed(self):
        return not self.player.participant.vars.get('game_ended', False)

    def get_players_for_group(self, waiting_players):
        print('new arrival!', 'round', self.round_number)
        print('waiting', waiting_players)
        if self.round_number == 1:
            if len(waiting_players) >= 2:
                print('round is 1, length is >= 2, match!')
                return waiting_players[:2]

        if self.round_number == 2:
            # remove one player to check against all other
            picked_player = waiting_players.pop()
            print('picked player', picked_player.id_in_subsession, 'old partner:', picked_player.in_round(1).partner)
            for player in waiting_players:
                print('test against:', player.id_in_subsession, 'old partner:', player.in_round(1).partner)
                if player.id_in_subsession == picked_player.in_round(1).partner \
                        or picked_player.participant.vars["game_ended"] \
                        or player.participant.vars["game_ended"]:
                    print('cannot match, have played with each other before')
                else:
                    print('match!')
                    return [picked_player, player]


class Decision(CustomMturkPage):
    template_name = "zero_shared/Decision.html"
    form_model = 'player'
    form_fields = ['choose_b']
    timeout_seconds = Constants.decision_timeout
    timeout_submission = {'choose_b': False}

    def is_displayed(self):
        return not self.player.participant.vars.get('game_ended', False)

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_decision = True
            self.player.end_game()
            self.group.dropout = True
        else:
            self.player.set_partner()


class Belief_choice_chance_1(CustomMturkPage):
    template_name = "zero_shared/Belief_choice_chance.html"

    form_model = 'player'
    form_fields = ['choice_chance_1']

    timeout_seconds = Constants.feelings_timeout
    timeout_submission = {'choice_chance_1': 0}

    def is_displayed(self):
        return self.round_number == 1 and not self.player.timeout_decision

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_feelings = True
            self.player.end_game()

    def vars_for_template(self):
        return {
            'second_time': False
        }


class Belief_color(CustomMturkPage):
    template_name = "zero_shared/Belief_color.html"
    form_model = 'player'
    form_fields = ['green_red']

    timeout_seconds = Constants.feelings_timeout
    timeout_submission = {'green_red': 0}

    def is_displayed(self):
        return not self.player.timeout_decision and not self.player.timeout_feelings and not self.player.participant.vars.get('game_ended', False)

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_feelings = True
            self.player.end_game()


class Belief_other(CustomMturkPage):
    template_name = "zero_shared/Belief_other.html"
    form_model = 'player'
    form_fields = ['a_or_b']

    timeout_seconds = Constants.feelings_timeout
    timeout_submission = {'a_or_b': 0}

    def is_displayed(self):
        return not self.player.timeout_decision and not self.player.timeout_feelings and not self.player.participant.vars.get('game_ended', False)

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_feelings = True
            self.player.end_game()


class DecisionWaitPage(WaitPage):
    def is_displayed(self):
        return (
                # not self.player.participant.vars.get('go_to_the_end', False) and
                # not self.group.dropout
                # not self.player.participant.vars.get('game_ended', False)
                True
        )

    body_text = "Please wait while your co-player makes the decision and answers the questions..."
    def after_all_players_arrive(self):
        self.group.draw_ball()
        self.group.get_coplayer_choices()
        self.group.calculate_round_payoffs()
        if self.round_number == Constants.num_rounds:
            self.group.set_final_payoffs()


class Results(CustomMturkPage):
    template_name = "zero_shared/Results.html"

    def is_displayed(self):
        return not self.group.dropout and not self.player.timeout_feelings and not self.player.timeout_decision and not self.player.participant.vars.get('game_ended', False)

    def vars_for_template(self):
        return {
            'own_choice': "B" if self.player.choose_b else "A",
            'own_implementation': "B" if self.player.implement_b else "A",
            'other_choice': "B" if self.player.other_choose_b else "A",
            'ball_color': "green" if self.group.ball_green else "red",
        }

class DropoutOther(CustomMturkPage):
    def is_displayed(self):
        return self.group.dropout

    def before_next_page(self):
        self.player.participant.vars['game_ended'] = True


class Belief_choice_chance_2(CustomMturkPage):
    template_name = "zero_shared/Belief_choice_chance.html"

    form_model = 'player'
    form_fields = ['choice_chance_2']

    def is_displayed(self):
        return self.round_number == 1 and not self.group.dropout and not self.player.timeout_feelings and not self.player.participant.vars.get('game_ended', False)

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_feelings = True
            self.player.end_game()

    def vars_for_template(self):
        return {
            'second_time': True
        }

class EndWaitExit(Page):
    def is_displayed(self):
        p1 = self.player.in_round(1)
        p2 = self.player.in_round(2)
        return self.player.participant.vars.get('go_to_the_end', False) \
                and self.round_number == Constants.num_rounds \
                and not p1.timeout_feelings and not p1.timeout_decision and not p2.timeout_feelings and not p2.timeout_decision

class DropoutExit(Page):
    def is_displayed(self):
        return self.player.participant.vars.get('go_to_the_end', False) \
               and self.round_number == Constants.num_rounds \
               and (
                    self.player.in_round(1).timeout_decision or self.player.in_round(1).timeout_feelings or
                    self.player.in_round(2).timeout_decision or self.player.in_round(2).timeout_feelings
               )



page_sequence = [
    GroupWaitPage,
    Decision,
    Belief_choice_chance_1,
    Belief_color,
    Belief_other,
    DecisionWaitPage,
    Results,
    DropoutOther,
    Belief_choice_chance_2,
    EndWaitExit,
    DropoutExit,
]
