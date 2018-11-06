from .base import *

DEBUG = False

ALLOWED_HOSTS = ['mysite.com', ]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.mailgun.org'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = config('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
#EMAIL_USE_TLS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangogirls',
        'USER': 'name',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}


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
