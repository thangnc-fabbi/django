from configs.settings.default_settings import *

MIDDLEWARE = MIDDLEWARE + [
    'base.middleware.QueryCountDebugMiddleware',
]
