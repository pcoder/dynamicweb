from .base import * # flake8: noqa

REGISTRATION_MESSAGE['message'] = REGISTRATION_MESSAGE['message'].format(host='dynamicweb-development.ungleich.ch',
                                                                         slug='{slug}')
ALLOWED_HOSTS = [
    "*"
    ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

INSTALLED_APPS += (
    'django_extensions',
    # debug_toolbar seems to conflict with multisite (and djangocms_multisite)
    'debug_toolbar',
    )

INTERNAL_IPS=('127.0.0.1',)

def show_toolbar(request):
    return True
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
}