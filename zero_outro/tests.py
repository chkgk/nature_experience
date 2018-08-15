from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):

        survey_answers = {
            'age': random.randint(13, 125),
            'gender': random.choice(['Male', 'Female', 'Other', 'I prefer not to tell']),
            'education': random.randint(0, 5),
            'major': random.choice(['Economics', 'Physics', 'Maths']),
            'risk': random.randint(0, 10)
        }

        yield SubmissionMustFail(pages.Survey, {})
        yield SubmissionMustFail(pages.Survey, {
            'age': random.randint(13, 125),
            'gender': random.choice(['Male', 'Female', 'Other', 'I prefer not to tell']),
            'education': random.randint(2, 5),
            'major': '',
            'risk': random.randint(0, 10)
        })
        yield (pages.Survey, survey_answers)
        yield (pages.LastPage)
