from .base import *

DEBUG = True

ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Your-db-name',
        'USER' : 'ur db-user-name'
        'PASSWORD' : 'ur-db-password'
        'HOST' : 'localhost',
        'PORT' : ''
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

STRIPE_PUBLIC_KEY = 'ur-live-PUBLIC-key'
STRIPE_SECRET_KEY = 'UR-LIVE-SECRET-KEY'