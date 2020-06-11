from configs.settings.default_settings import *

MIDDLEWARE = MIDDLEWARE + [
    'base.middleware.QueryCountDebugMiddleware',
]

DEBUG = True
ALLOWED_HOSTS = ['*']

try:
    from .local_settings import *
except:
    print('Develop local setting not found')
