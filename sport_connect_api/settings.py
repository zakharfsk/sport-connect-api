"""
Django settings for sport_connect_api project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

from corsheaders.defaults import default_methods, default_headers
from django.contrib.admin import AdminSite
from environs import Env

"""
Модель Спорт школи

Адреса школа(вибирається з карти в адмінці)
https://django-map-widgets.readthedocs.io
Сайт школи(юрла)

Вибір школи з випадаючого списку
Вибір класу з випадаючого списку, окремо цифра окремо буква
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(f'{BASE_DIR / ".env"}')

CALCULATIONS_FILES_FOLDER = os.path.join(BASE_DIR, 'media/calculations')

if not os.path.exists(CALCULATIONS_FILES_FOLDER):
    os.makedirs(CALCULATIONS_FILES_FOLDER)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS') if not DEBUG else ['*']
CSRF_TRUSTED_ORIGINS = env.list('DJANGO_ALLOWED_HOSTS') if not DEBUG else []

# CORS Settings
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = env.list('DJANGO_CORS_ORIGIN_WHITELIST') if not DEBUG else []
CORS_ALLOWED_ORIGIN_REGEXES = env.list('CORS_ALLOWED_ORIGIN_REGEXES') if not DEBUG else []

CORS_ALLOW_HEADERS = default_headers
CORS_ALLOW_METHODS = default_methods

# Application definition

INSTALLED_APPS = [
    # asgi
    "channels",
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-Party Apps
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'rest_framework_simplejwt',
    # Local Apps
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'sport_connect_api.middleware.JWTAuthMiddleware',
]

ROOT_URLCONF = 'sport_connect_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'sport_connect_api.wsgi.application'
ASGI_APPLICATION = "sport_connect_api.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env.str("REDIS_URL") + "0"],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASSWORD'),
        'HOST': env.str('DATABASE_HOST'),
        'PORT': env.int('DATABASE_PORT')
    }
}

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

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# redis://redis:6380/0
CELERY_BROKER_URL = env.str("REDIS_URL") + "1"
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3000}
CELERY_RESULT_BACKEND = env.str("REDIS_URL") + "1"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

# REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=env.int("ACCESS_TOKEN_LIFETIME", default=1)),  # timedelta(hours=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=env.int("REFRESH_TOKEN_LIFETIME", default=2)),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(hours=3),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

AdminSite.index_template = 'admin.html'

LIST_TOPICS = [
    "id",
    "Ім'я",
    "Прізвище",
    "Стать",
    "Вік",
    "Школа",
    "Клас",
    "Зріст, см",
    "Маса, гр",
    "Периметр плеча напруженого, см",
    "Периметр плеча розслабленого, см",
    "Ширина рук, см",
    "Біг 30 м, с",
    "Стрибок з місця у довжину, см",
    "Кидок набивного м’яча на дальність (1 кг), м",
    "Піднімання тулуба в сід за 60с, кількість",
    "Згинання розгинання рук в упорі лежачи, кількість",
    "Нахил тулуба стоячи (нахили тулуба вперед з положення сидячи), см",
    "Човниковий біг (4х9 м), с",
    "Швидкість реакції (ловля палиця, яка має сантиметрові помітки), см",
    "Стрибки на скакалці за 60 с, кількість",
    "Ширина плечей, см",
    "Викрут мірної лінійки, см",
]

LIST_STANDARDS = [
    "Зріст, см",
    "Вагової-ростовий індекс (індекс маси тіла)",
    "Індекс розвитку мускулатури (периметр плеча напруженого/периметр плеча розслабленого)",
    "Співвідношення розмаху рук до довжини тіла стоячи, см",
    "Біг 30м, с",
    "Стрибок з місця у довжину, см",
    "Кидок набивного м’яча на дальність (1 кг), м",
    "Підіймання тулуба в сід за 60с, кількість",
    "Згинання розгинання рук в упорі лежачи, кількість",
    "Нахил тулуба стоячи (нахили тулуба вперед з положення сидячи), см",
    "Човниковий біг (4х9м), с",
    "Швидкість реакції (ловля палиця, яка має сантиметрові помітки), см",
    "Стрибки на скакалці за 60с, кількість",
    "Викрут мірної лінійки (різниця від ширини плечей), см"
]
