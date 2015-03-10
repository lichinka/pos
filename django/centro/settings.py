# coding=utf-8
#
# Django settings for the Centro project.
#
import os

APPLICATION_NAME = 'CenTro'
APPLICATION_VERSION = '0.1.5.3'
THIS_TERMINAL_ID = '1'

PROJECT_ROOT = os.path.abspath (os.path.dirname (__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'centro.db',                     # Or path to database file if using sqlite3.
        'USER': '',                           # Not used with sqlite3.
        'PASSWORD': '',                       # Not used with sqlite3.
        'HOST': '',                           # Set to empty string for localhost.
        'PORT': '',                           # Set to empty string for default.
        #
        # Settings for the testing database
        #
        'TEST_NAME': 'centro_test.db',
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_bin',
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Ljubljana'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

#LANGUAGE_CODE = 'en'
#LANGUAGE_CODE = 'es'
LANGUAGE_CODE = 'sl'

#
# Available languages for this project
#
ugettext = lambda s: s          # dummy ugettext function, 
                                # as Django's docs dictate

LANGUAGES = (
    ('sl', ugettext ('Slovenščina')),
    ('en', ugettext ('English')),
)
 
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://localhost:8000/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l1)m+43si3vyz!sc4=)79z+%snmhmth5n4!g83k9l62vbgc_26'

# The URL of the admin interface
ADMIN_URL = '/admin'

# Redirect to this address after a successful login
LOGIN_REDIRECT_URL = ADMIN_URL

# Our custom model to house extra data for the users
AUTH_PROFILE_MODULE = 'accounts.UserProfile'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'centro.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # 'django.contrib.sites',
    # 'django.contrib.messages',
    'multilingual_model',
    'centro.utils',
    'centro.accounts',
    'centro.modules',
    'centro.companies',
    'centro.items',
    'centro.stock',
    'centro.sales'
)

#
# Setup logging
#
import logging, time

LOG_FILENAME = PROJECT_ROOT + '/logs/' + time.strftime ('%Y-%m-%d') + '.log'

logging.basicConfig (filename=LOG_FILENAME, level=logging.DEBUG)
logging.debug ('Logging debug facility re-started ...')

#
# Synchronize Python locale with Django settings
#
import locale

mylocale = 'en_US'
if (LANGUAGE_CODE == 'en'):
    mylocale = 'en_US'
elif (LANGUAGE_CODE == 'es'):
    mylocale = 'es_AR'
elif (LANGUAGE_CODE == 'sl'):
    mylocale = 'sl_SI'

locale.setlocale (locale.LC_ALL, (mylocale, 'UTF-8'))
logging.debug ('Python locale set to %s' % mylocale)

