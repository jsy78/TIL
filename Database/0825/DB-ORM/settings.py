import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

INSTALLED_APPS = ("db","django_extensions")


# https://docs.djangoproject.com/en/4.0/topics/logging/
"""
# 쿼리문 출력 설정 코드
DEBUG = True
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
    },
    "handlers": {
        "debug-console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["debug-console"],
        },
    },
}
"""