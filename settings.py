from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.50,
    'doc': "",
    'experimenter_name': "Christian König-Kersting",
    'experimenter_email': "christian.koenig@awi.uni-heidelberg.de",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'zero_intro_human',
        'display_name': "Human - Intro",
        'num_demo_participants': 1,
        'app_sequence': ['zero_intro'],
        'treatment': 'human'
    },
    {
        'name': 'zero_main_human',
        'display_name': "Human - Main Part",
        'num_demo_participants': 4,
        'app_sequence': ['zero_main_human'],
    },
    {
        'name': 'zero_outro_human',
        'display_name': "Human - Outro",
        'num_demo_participants': 1,
        'app_sequence': ['zero_outro'],
        'treatment': 'human'
    },
    {
        'name': 'zero_human',
        'display_name': "Human - Full Experiment",
        'num_demo_participants': 4,
        'app_sequence': ['zero_intro', 'zero_main_human', 'zero_outro'],
        'treatment': 'human'
    },
    {
        'name': 'zero_intro_bot',
        'display_name': "Computer - Intro",
        'num_demo_participants': 1,
        'app_sequence': ['zero_intro'],
        'treatment': 'computer'
    },
    {
        'name': 'zero_main_bot',
        'display_name': "Computer - Main Part",
        'num_demo_participants': 1,
        'app_sequence': ['zero_main_bot'],
        'treatment': 'computer'
    },
    {
        'name': 'zero_outro_bot',
        'display_name': "Computer - Outro",
        'num_demo_participants': 1,
        'app_sequence': ['zero_outro'],
        'treatment': 'computer'
    },
    {
        'name': 'zero_bot',
        'display_name': "Computer - Full Experiment",
        'num_demo_participants': 1,
        'app_sequence': ['zero_intro', 'zero_main_bot', 'zero_outro'],
        'treatment': 'computer'
    },
    # {
    #     'name': 'zero_main_outro_human',
    #     'display_name': "Human - Main Part and Outro",
    #     'num_demo_participants': 4,
    #     'app_sequence': ['zero_main_human', 'zero_outro'],
    #     'treatment': 'human'
    # },
]

mturk_hit_settings = {
    'keywords': ['bonus', 'study', 'decision making'],
    'title': 'Research in decision making',
    'description': 'Participate in a game and a short survey. Please note that the task is to be completed within 10-15 minutes as you are matched with a co-player.',
    'frame_height': 500,
    'preview_template': 'zero_intro/MTurkPreview.html',
    'minutes_allotted_per_assignment': 25,
    'expiration_hours': 3 * 24,  # 3 days
    # PRODUCTION ONLY
    # this would grant florians qualification, if we run it through his account.
    # 'grant_qualification_id': '3DA2M59FDW8FXK3OTJT76I16UG0RXG',# to prevent retakes

    # alternatively, if we use Christian's account:
    #'grant_qualification_id': '3X4G950TG9JM27SOMLGT6VJ1IU8P1C',
    # SANDBOX ONLY

    # 'grant_qualification_id': '3TW6VZEPPW5UL7N9GRPX9CW4P7VXPS',# to prevent retakes
    'qualification_requirements': [
        # # PRODUCTION ONLY
        # {
        #     'QualificationTypeId': "00000000000000000071",
        #     'Comparator': "EqualTo",
        #     'LocaleValues': [{'Country': "US"}]
        # },
        # # qualification granted by Florian's Experiments
        # {
        #     'QualificationTypeId': "3DA2M59FDW8FXK3OTJT76I16UG0RXG",
        #     'Comparator': "DoesNotExist",
        # },
        # # qualification granted by Christian's runs
        # {
        #     'QualificationTypeId': "3X4G950TG9JM27SOMLGT6VJ1IU8P1C",
        #     'Comparator': "DoesNotExist",
        # }
        # SANDBOX ONLY
        # {
        #    'QualificationTypeId': "3TW6VZEPPW5UL7N9GRPX9CW4P7VXPS",
        #    'Comparator': "DoesNotExist",
        # }
    ],
}

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

DEMO_PAGE_INTRO_HTML = """Choose an option on the right to test individual parts or the full treatment conditions."""

# don't share this with anybody.
SECRET_KEY = '(js*7-e9%&_d*0j3%0jd&m$_)qvppc0tp_%7pzhqq-mt8=k6k@'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
EXTENSION_APPS = ['otree_mturk_utils']

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')