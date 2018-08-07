from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Decision1(Page):
    pass

class Decision2(Page):
    pass

class Belief_choice_chance_1 (Page):
    pass

class Belief_color_1 (Page):
    pass

class Belief_other_1 (Page):
    pass

class Belief_choice_chance_2 (Page):
    pass

class Belief_color_2 (Page):
    pass

class Belief_other_2 (Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Decision1,
    Decision2,
    Belief_choice_chance_1,
    Belief_color_1,
    Belief_other_1,
    Belief_choice_chance_2,
    Belief_color_2,
    Belief_other_2,

]
