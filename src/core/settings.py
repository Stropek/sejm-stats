"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import datetime
from pathlib import Path
from urllib.parse import urljoin

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: DEBUG}

ALLOWED_HOSTS = [
    "sejm-stats.pl",
    "www.sejm-stats.pl",
    "*.wikipedia.org",
    "api.sejm.gov.pl",
    "145.239.29.193",
    "localhost",
    "127.0.0.1",
    "127.0.0.1:3000",
    "app",
]
CSRF_TRUSTED_ORIGINS = [
    "https://sejm-stats.pl",
    "https://www.sejm-stats.pl",
    "https://*.wikipedia.org",
    "https://api.sejm.gov.pl",
    "http://127.0.0.1",
    "https://sejm.aleksander-kowalski.pl",
]
API_URL_ROOT = "/apiInt"

# Application definition

INSTALLED_APPS = [
    "meta",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "fontawesomefree",
    "django_select2",
    "drf_redesign",
    "rest_framework",
    "crispy_forms",
    "corsheaders",
    "django_filters",
    "django_celery_results",
    "crispy_bootstrap5",
    "ckeditor",
    "rolepermissions",
    "api.apps.ApiConfig",
    "sejm_app.apps.SejmAppConfig",
    "community_app.apps.ArticlesAppConfig",
    "eli_app.apps.EliAppConfig",
]
if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True


if DEBUG:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("DATABASE_HOST"),
        "PORT": config("POSTGRES_PORT"),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"


REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 2,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
}

# Meta settings
META_SITE_PROTOCOL = "https"
META_SITE_DOMAIN = "sejm-stats.pl"
META_SITE_TYPE = "website"
META_SITE_NAME = "Sejm Stats"
META_INCLUDE_KEYWORDS = [
    "Sejm",
    "parlament",
    "polska",
    "posłowie",
    "dane sejmowe",
    "głosowania",
    "wydatki parlamentarne",
    "statystyki sejmowe",
    "AI",
    "Artykuły",
    "Michał Skibiński",
    "analiza polityczna",
]
# META_USE_OG_PROPERTIES = True
# META_USE_TWITTER_PROPERTIES = True
# META_USE_SCHEMAORG_PROPERTIES = True
META_USE_TITLE_TAG = True

META_USE_SITES = False

# Internationalization
LANGUAGE_CODE = "pl"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = "/code/static"

MEDIA_URL = "/media/"
MEDIA_ROOT = "/code/media"
ADMINS = [("Michal", "skibinek109@gmail.com")]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

API_URL = "https://api.sejm.gov.pl/"
PATRONITE_API_URL = "https://patronite.pl/author-api/"
PATRONITE_API_TOKEN = config("PATRONITE_API_TOKEN", default="")

TERM = 10
TERM_START_DATE = datetime.date(2023, 11, 13)

SEJM_ROOT_URL = urljoin(API_URL, f"sejm/term{TERM}")
ENVOYS_URL = urljoin(API_URL, f"sejm/term{TERM}/MP")
CLUBS_URL = urljoin(API_URL, f"sejm/term{TERM}/clubs")
VOTINGS_URL = urljoin(API_URL, f"sejm/term{TERM}/votings")
RESOLUTION_URL = "https://orka.sejm.gov.pl/proc10.nsf/uchwaly"


# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "sejmstats@gmail.com"  # Your Gmail address


# CELERY
CELERY_TIMEZONE = "Europe/Warsaw"
CELERY_TASK_SERIALIZER = "pickle"
CELERY_RESULT_SERIALIZER = "pickle"
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_ACCEPT_CONTENT = ["pickle"]
CELERY_RESULT_BACKEND = "django-db"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module}  {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
    },
}


SILENCED_SYSTEM_CHECKS = ["ckeditor.W001"]

CACHE_MIDDLEWARE_SECONDS = 0
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

if not config("DEBUG", default=False, cast=bool):
    CACHE_MIDDLEWARE_SECONDS = 60 * 15
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 2592000  # 30 days # https://hstspreload.org/
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://redis:6379/1",  # Assuming your Redis service is named 'redis' in docker-compose and using DB 1
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            "KEY_PREFIX": "sejm_stats",  # Optional: Prefix for your cache keys to avoid conflicts
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
# SECURE_SSL_REDIRECT = True
