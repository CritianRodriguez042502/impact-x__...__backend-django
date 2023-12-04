"""
Django settings for agency_server project.
Django version = 4.2.4.
"""
from django.conf import settings
import dj_database_url
from datetime import timedelta
from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-wzc4@35lmrbnxmm7$0xhbsw*ol6x)-#7nw#hv+c9ng^#!jl6ch'
# --- SECRET KEY DEPLOY ---
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Default apps
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

APPS_PROJECT = [
    'apps.user_system',
    'apps.blog',
    'apps.dashboard',
    'apps.blog_reactions',
    'apps.api_bbc_news',
]

LIBRERIS = [
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'social_django',
    'corsheaders',
    'ckeditor',
    'ckeditor_uploader',
]

INSTALLED_APPS = []
INSTALLED_APPS.extend(DEFAULT_APPS)
INSTALLED_APPS.extend(APPS_PROJECT)
INSTALLED_APPS.extend(LIBRERIS)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agency_server.urls'
WSGI_APPLICATION = 'agency_server.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

if not DEBUG:   
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

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
                #### Google ####
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# ---------------------------------------
# Data base

if 'RENDER' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default='postgresql://postgres:postgres@localhost/postgres',
        )
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

#------------------------------------------

# Password validation
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
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

# ADDITIONAL SETTINGS DJANGO ____________________________________________________________________

#more middelware
MIDDLEWARE.insert(0,'corsheaders.middleware.CorsMiddleware')
MIDDLEWARE.insert(1,'social_django.middleware.SocialAuthExceptionMiddleware')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Config ckeditor
CKEDITOR_CONFIGS = {
    'ckeditor': {'toolbar': 'Full',}
    }

CKEDITOR_UPLOAD_PATH = "/media/"

# Cors headers
CORS_ALLOWED_ORIGINS = [
    "https://impact-x.onrender.com",
    "https://api-news-v2.onrender.com",
    "https://web-portfolio-z9ym.onrender.com",
]

CORS_ORIGIN_WHITELIST = [
    "https://impact-x.onrender.com",
    "https://api-news-v2.onrender.com",
    "https://web-portfolio-z9ym.onrender.com",
]

CORS_ALLOW_CREDENTIALS = True

# Password hashers
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

#Auth backend
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

# Rest_framewook_settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

# Config email with django
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_BACKEND', cast=str)
EMAIL_HOST_PASSWORD = config('EMAIL_BACKEND_PASSWORD', cast=str)


# Domain
DOMAIN = 'impact-x.onrender.com'

# Custom user model
AUTH_USER_MODEL = "user_system.Model_users"

# Djoser Config
DJOSER = {
    'LOGIN_FIELD': 'email',
    'PASSWORD_RESET_CONFIRM_URL': 'admin/reset_password/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'admin/reset_username/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'admin/user/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'RESEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    
    #### Google ####
    'SOCIAL_AUTH_TOKEN_STRATEGY': "apps.user_system.strategy.TokenStrategy",
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [
        "https://github.com/CritianRodriguez042502/agency_view/#/access/signin"
        ],
    
    'SERIALIZERS': {},
    
    'EMAIL': {
        'activation': 'apps.user_system.email.Activation',
        'confirmation': 'apps.user_system.email.Confirmation',
        'password_reset': 'apps.user_system.email.PasswordReset',
        'password_changed_confirmation': 'apps.user_system.email.PasswordChangedConfirmation',
    },
}

# Access with google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_CLIENT_ID', cast = str)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_CLIENT_SECRET', cast = str)
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name', 'username']

# Config JWT
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ["JWT"],
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10000),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "AUTH_TOKEN_CLASESS" : ("rest_framework_simplejwt.tokens.AccessToken",),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
}

