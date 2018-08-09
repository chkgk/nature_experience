from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.50,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'zero_intro_human',
        'display_name': "Intro - Human",
        'num_demo_participants': 1,
        'app_sequence': ['zero_intro'],
        'treatment': 'human'
    },
    {
        'name': 'zero_main_1_human',
        'display_name': "Decision Part 1 - Human",
        'num_demo_participants': 4,
        'app_sequence': ['zero_main_human'],
        'treatment': 'human',
        'decision1': True,
    },
    {
        'name': 'zero_main_2_human',
        'display_name': "Decision Part 2 - Human",
        'num_demo_participants': 4,
        'app_sequence': ['zero_main_human'],
        'treatment': 'human',
        'decision1': False,
    },
    {
        'name': 'zero_outro_human',
        'display_name': "Outro - Human",
        'num_demo_participants': 1,
        'app_sequence': ['zero_outro'],
        'treatment': 'human'
    },
    {
        'name': 'zero_human',
        'display_name': "Full Experiment - Human",
        'num_demo_participants': 1,
        'app_sequence': ['zero_intro', 'zero_main_human', 'zero_main_human', 'zero_outro'],
        'treatment': 'human'
    },
    {
        'name': 'zero_intro_bot',
        'display_name': "Intro - Computer",
        'num_demo_participants': 1,
        'app_sequence': ['zero_intro'],
        'treatment': 'computer'
    },
    {
        'name': 'zero_main_bot',
        'display_name': "Main Part - Computer",
        'num_demo_participants': 1,
        'app_sequence': ['zero_main_bot'],
        'treatment': 'computer'
    },
    {
        'name': 'zero_main_1_bot',
        'display_name': "Decision Part 1 - Computer",
        'num_demo_participants': 1,
        'app_sequence': ['zero_main_bot'],
        'treatment': 'computer',
        'decision1': True,
    },
    {
        'name': 'zero_main_1_bot',
        'display_name': "Decision Part 2 - Computer",
        'num_demo_participants': 1,
        'app_sequence': ['zero_main_bot'],
        'treatment': 'computer',
        'decision1': False
    },
    {
        'name': 'zero_outro_bot',
        'display_name': "Outro - Computer",
        'num_demo_participants': 1,
        'app_sequence': ['zero_outro'],
        'treatment': 'computer'
    },
    {
        'name': 'zero_bot',
        'display_name': "Full Experiment - Computer",
        'num_demo_participants': 1,
        'app_sequence': ['zero_intro', 'zero_main_1_bot', 'zero_main_2_bot', 'zero_outro'],
        'treatment': 'computer'
    },
    {
       'name': 'Game',
       'display_name': "All Apps - New Instructions",
       'num_demo_participants': 1,
       'app_sequence': ['zero_intro', 'zero_main_bot', 'zero_main_human', 'zero_outro'],

    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = []

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# Consider '', None, and '0' to be empty/false
DEBUG = (environ.get('OTREE_PRODUCTION') in {None, '', '0'})

DEMO_PAGE_INTRO_HTML = """ """

# don't share this with anybody.
SECRET_KEY = '(js*7-e9%&_d*0j3%0jd&m$_)qvppc0tp_%7pzhqq-mt8=k6k@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
EXTENSION_APPS = ['otree_mturk_utils']
