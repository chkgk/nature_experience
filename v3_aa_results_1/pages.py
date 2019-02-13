from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FakeGrouping(Page):
    timeout_seconds = 5

    def before_next_page(self):
        self.player.draw_ball()
        for player in self.group.get_players():
            player.set_partner_action()
            player.calculate_round_payoff()


class Results(Page):

    def vars_for_template(self):
        return {
            'own_action': 'B' if self.player.action else 'A',
            'others_action': 'B' if self.player.others_action else 'A',
            'ball_color': 'green' if self.player.ball_green else 'red',
        }


page_sequence = [
    FakeGrouping,
    Results
]
