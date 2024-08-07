"""
Django settings for storefront project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

import os
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'


DEBUG = True

ALLOWED_HOSTS = ['192.168.1.11']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',    'djoser',

  
    'debug_toolbar'
 
    ,'booking'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
  

    'django.middleware.security.SecurityMiddleware',    
        # "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]



INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
# ----
ROOT_URLCONF = 'storefront.urls'

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

WSGI_APPLICATION = 'storefront.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'ali',
     'USER': 'ali',
      'HOST': '127.0.0.1',
    #   "PORT": "2222",
    'PASSWORD': 'asdzxcasd',
  }
  }

# set
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = '/static/'
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')



# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# here we change the main user auth class 
# to make email field unique 
# CUSTOMIZING THE USER MODEL
# AUTH_USER_MODEL='coree.User'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
       
    ),
}

# DJOSER = {

#     'SERIALIZERS': {
      
#    'user_create': 'coree.serializers.UserCreateSerializer',
#    'current_user': 'coree.serializers.CurrentUserSerializer',

#     },
# }
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),}