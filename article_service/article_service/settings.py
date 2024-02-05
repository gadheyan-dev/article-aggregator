"""
Django settings for article_service project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import mongoengine

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4^0n9b%_x1hk9$=g5bxfnne2@hh!#rzcl3c&4hc52ja+2l@-7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_mongoengine',
    'articles'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'article_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'article_service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'djongo',
        # 'NAME': os.environ.get('MONGO_INITDB_DATABASE', 'articles_db'),
        # 'ENFORCE_SCHEMA': False,
        # 'CLIENT': {
        #     'host': 'mongodb://article_user:article_password@article_db:27017/'
        #     # 'HOST': os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'localhost'),
        #     # 'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        #     # 'USER': os.environ.get('POSTGRES_USER', 'articles_user'),
        #     # 'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'articles_password'),
        # }

    }
}

MONGO_DATABASES = {
    'default': {
        'NAME': 'article_db',
        'HOST': 'article_db',
        'PORT': 27017,
        'USERNAME': 'article_user',
        'PASSWORD': 'article_password',
        'ALIAS': 'default',
    },
}
mongoengine.connect(
    db=MONGO_DATABASES['default']['NAME'],
    host=MONGO_DATABASES['default']['HOST'],
    port=MONGO_DATABASES['default']['PORT'],
    username=MONGO_DATABASES['default']['USERNAME'],
    password=MONGO_DATABASES['default']['PASSWORD'],
    alias=MONGO_DATABASES['default']['ALIAS']
)


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',  # Set the desired log level (INFO, DEBUG, etc.)
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',  # Set the desired log level for Django's own logs
        },
        'gunicorn.access': {
            'handlers': ['console'],
            'level': 'INFO',  # Set the desired log level for Gunicorn access logs
            'propagate': False,
        },
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/app/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
