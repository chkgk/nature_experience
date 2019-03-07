from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage



class Grouping(CustomMturkWaitPage):
    template_name = "v3_results_2/GroupingWaitPage.html"
    group_by_arrival_time = True
    startwp_timer = 115  # 115s + 5s fake wait = 120s
    skip_until_the_end_of = 'experiment'

    def get_players_for_group(self, waiting_players):
        print('new arrival!', 'round', self.round_number)
        print('waiting', waiting_players)

        # remove one player to check against all other
        picked_player = waiting_players.pop()
        print('picked player', picked_player.id_in_subsession, 'old partner:', picked_player.participant.vars.get('partner_1'))
        for player in waiting_players:
            print('test against:', player.id_in_subsession, 'old partner:', player.participant.vars.get('partner_1'))
            if player.id_in_subsession == picked_player.participant.vars.get('partner_1'):
                print('cannot match, have played with each other before')
            else:
                print('match!')
                return [picked_player, player]

    def after_all_players_arrive(self):
        # if participant leaves the study, they end up in a group of 1.
        if len(self.group.get_players()) == 1:
            return

        self.group.draw_ball()
        for player in self.group.get_players():
            player.set_partner_action()
            player.calculate_round_payoff()



class Results(CustomMturkPage):

    def vars_for_template(self):
        return {
            'own_action': 'B' if self.player.action else 'A',
            'others_action': 'B' if self.player.others_action else 'A',
            'ball_color': 'green' if self.group.ball_green else 'red',
        }


page_sequence = [
    Grouping,
    Results,
]
