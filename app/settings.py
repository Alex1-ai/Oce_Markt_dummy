"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import os
from dotenv import load_dotenv
#from decouple import config
from django.contrib.messages import constants as messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY= os.environ.get('SECRET_KEY', "secret-key-if-not-configured-in-environment")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = [ "*", "oce-markt.onrender.com", "oce-markt.com"]


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.auth.password_validation',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',
    'category',
    'accounts',
    'store',
    'carts',
    'orders',
    'admin_honeypot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # for automatically logging out user when is inactive
    # 'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

# seesion timeout

# SESSION_EXPIRE_SECONDS = 3600  # 1 hour
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# SESSION_TIMEOUT_REDIRECT = 'accounts/login'
ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# if 'RDS_DB_NAME' in os.environ:
#     DATABASES = {
#         'default':{
#             'ENGINE':'django.db.backends.postgresql',
#             'NAME': os.environ['RDS_DB_NAME'],
#             'USER': os.environ['RDS_USERNAME'],
#             'PASSWORD': os.environ['RDS_PASSWORD'],
#             'HOST': os.environ['RDS_HOSTNAME'],
#             'PORT': os.environ['RDS_PORT']
#         }
#     }



# else:
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',

    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,

        }


    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#         'OPTIONS': {
#             'min_length': 8,
#         },
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#         'OPTIONS': {
#             'user_attributes': ('username', 'email'),
#         }
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumUppercaseValidator',
#         'OPTIONS': {
#             'min_uppercase': 1,
#         }
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLowercaseValidator',
#         'OPTIONS': {
#             'min_lowercase': 1,
#         }
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumDigitValidator',
#         'OPTIONS': {
#             'min_digits': 1,
#         }
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumSpecialCharacterValidator',
#         'OPTIONS': {
#             'min_special_characters': 1,
#         }
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID '
# AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
# AWS_STORAGE_BUCKET_NAME = 'AWS_STORAGE_BUCKET_NAME'
# AWS_S3_SIGNATURE_NAME = 's3v4',
# AWS_S3_REGION_NAME = 'AWS_S3_REGION_NAME'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL =  None
# AWS_S3_VERITY = True
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = BASE_DIR/'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# MEDIA FILES

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',

}


# SMTP CONFIGURATION
# email stuff
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# EMAIL_PORT = os.environ.get('EMAIL_PORT')


EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_ACTIVE_FIELD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_SERVER = os.environ.get('EMAIL_SERVER')

EMAIL_HOST_PASSWORD =os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')


ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
EMAIL_USE_TLS=True
EMAIL_PORT=587


# DELIVERY FEE
STANDARD_DELIVERY = 5

# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_SIGNATURE_NAME = os.environ.get('AWS_S3_SIGNATURE_NAME'),
# AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
# AWS_S3_FILE_OVERWRITE = os.environ.get('AWS_S3_FILE_OVERWRITE')
# AWS_DEFAULT_ACL =  os.environ.get('AWS_DEFAULT_ACL')
# AWS_S3_VERITY = os.environ.get('AWS_S3_VERITY')
# DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE')
# AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SIGNATURE_NAME=os.environ.get('AWS_S3_SIGNATURE_NAME')
AWS_S3_REGION_NAME=os.environ.get('AWS_S3_REGION_NAME')
AWS_S3_FILE_OVERWRITE=False
AWS_DEFAULT_ACL=None
AWS_S3_VERITY=True
DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE')