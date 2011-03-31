from pkg_resources import resource_filename

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web369',
        'USER': 'root',
        'PASSWORD': '',
    }
}

TIME_ZONE = 'Europe/Vilnius'
LANGUAGE_CODE = 'lt'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'
STATIC_ROOT = resource_filename('web369', '../../var/htdocs/static')
STATICFILES_DIRS = (
    resource_filename('web369', 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = resource_filename('web369', '../../var/htdocs/media')
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

SECRET_KEY = 'SBX*YTL!cANetM&uFTf6R5Je(@PX3!rtgo)kgwNT'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'web369.urls.default'

TEMPLATE_DIRS = (
    resource_filename('web369', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'web369',
)