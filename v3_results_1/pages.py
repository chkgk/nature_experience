from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from otree_mturk_utils.views import CustomMturkPage, CustomMturkWaitPage



class Grouping(CustomMturkWaitPage):
    template_name = "v3_results_1/GroupingWaitPage.html"
    group_by_arrival_time = True
    startwp_timer = 5  # 115s +5s fake wait = 120s
    skip_until_the_end_of = 'experiment'

    def get_players_for_group(self, waiting_players):
        print('new arrival!', 'round', self.round_number)
        print('waiting', waiting_players)

        if len(waiting_players) >= 2:
            print('round is 1, length is >= 2, match!')
            return waiting_players[:2]


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
