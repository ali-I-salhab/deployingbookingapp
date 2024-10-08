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
from firebase_admin import initialize_app,credentials
   

import os

from httplib2 import Credentials
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
 
    ,'booking','core','social_django',    "fcm_django"

]
cred = credentials.Certificate('/home/ali--salhab/Desktop/djangoproject2024/storefront2/elite-antenna-346019-firebase-adminsdk-d1tp6-576afae9ac.json')
FIREBASE_APP = initialize_app(cred)

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
  

    'django.middleware.security.SecurityMiddleware',    
        # "whitenoise.middleware.WhiteNoiseMiddleware",
            "social_django.middleware.SocialAuthExceptionMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]



FCM_DJANGO_SETTINGS = {
     # an instance of firebase_admin.App to be used as default for all fcm-django requests
     # default: None (the default Firebase app)
    "DEFAULT_FIREBASE_APP": None,
     # default: _('FCM Django')
    # "FCM_SERVER_KEY": "AAAAEz03a4c:APA91bErjFYnq4Lkx3XwXn38apQqdZHLfmeC_3GyswSjDQrCHSbuBHEymWlVfI8uTDSDka9vC4a9oG42WKmUQFM_g77Mv9BL9SakPZMrTdQaE69rXzC5AD1iQM2vKx_VIYf9h_IP3tnh",

    "APP_VERBOSE_NAME": "django_fcm",
     # true if you want to have only one active device per registered user at a time
     # default: False
    "ONE_DEVICE_PER_USER": True,
     # devices to which notifications cannot be sent,
     # are deleted upon receiving error response from FCM
     # default: False
    "DELETE_INACTIVE_DEVICES": True,
}
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
                                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
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
AUTH_USER_MODEL='core.User'
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING':False,
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated'

    ],
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

# DJOSER = {
#     'LOGIN_FIELD': 'email'
# }
DJOSER = {
    'LOGIN_FIELD': 'email',
       'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    # 'USER_CREATE_PASSWORD_RETYPE': True,
    'SERIALIZERS': {
        'user_create': 'core.serializer.CustomSerilizer',
        # 'user': 'accounts.serializers.UserCreateSerializer',
        # 'current_user': 'accounts.serializers.CurrentUserSerializer'
    
    }
    
    }
DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    # "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    # "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_PASSWORD_RETYPE": True,
    'USERNAME_RESET_CONFIRM_URL':"http://192.168.1.11:8000/auth/users/reset_email/a.html",
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",


    "ACTIVATION_URL": "activate/{uid}/{token}",

    
    "SEND_ACTIVATION_EMAIL": True,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": ["http://localhost:3000"],
    "SERIALIZERS": {
           'user_create': 'core.serializer.CustomSerilizer',
        # "user_create": "accounts.serializers.UserCreateSerializer",
        "user":'core.serializer.CustomSerilizer',
        "current_user": 'core.serializer.CustomSerilizer',
        "user_delete": "djoser.serializers.UserDeleteSerializer",
        "me":'core.serializer.CustomSerilizer',
    },
}


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'alisalhab258@gmail.com'
EMAIL_HOST_PASSWORD = 'hxbb oykz ubbm nkmy'
