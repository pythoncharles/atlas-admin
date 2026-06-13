from pathlib import Path

import pymysql
from pydantic_settings import BaseSettings, SettingsConfigDict

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    django_secret_key: str = "test-secret-key-with-at-least-32-bytes"
    django_debug: bool = False
    django_allowed_hosts: str = "127.0.0.1,localhost"

    mysql_host: str = "127.0.0.1"
    mysql_port: int = 3306
    mysql_database: str = "atlas_db"
    mysql_business_database: str | None = None
    mysql_user: str = "atlas_admin_ro"
    mysql_password: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()

SECRET_KEY = settings.django_secret_key
DEBUG = settings.django_debug
ALLOWED_HOSTS = [host.strip() for host in settings.django_allowed_hosts.split(",") if host.strip()]

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.import_export",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.users",
    "apps.assessments",
    "apps.reports",
    "apps.goals",
    "apps.daily",
    "apps.weekly",
    "apps.payments",
    "apps.ai",
    "apps.shares",
    "apps.files",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "atlas_admin.urls"
WSGI_APPLICATION = "atlas_admin.wsgi.application"
ASGI_APPLICATION = "atlas_admin.asgi.application"

business_database_name = settings.mysql_business_database or settings.mysql_database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": settings.mysql_host,
        "PORT": settings.mysql_port,
        "NAME": settings.mysql_database,
        "USER": settings.mysql_user,
        "PASSWORD": settings.mysql_password,
        "OPTIONS": {"charset": "utf8mb4"},
    },
    "business": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": settings.mysql_host,
        "PORT": settings.mysql_port,
        "NAME": business_database_name,
        "USER": settings.mysql_user,
        "PASSWORD": settings.mysql_password,
        "OPTIONS": {"charset": "utf8mb4"},
    },
}

if settings.mysql_database == ":memory:":
    DATABASES = {
        "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
        "business": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
    }

DATABASE_ROUTERS = ["common.db_router.BusinessDatabaseRouter"]

LANGUAGE_CODE = "zh-hans"
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIGRATION_MODULES = {
    "users": None,
    "assessments": None,
    "reports": None,
    "goals": None,
    "daily": None,
    "weekly": None,
    "payments": None,
    "ai": None,
    "shares": None,
    "files": None,
}

UNFOLD = {
    "SITE_TITLE": "Atlas Admin",
    "SITE_HEADER": "Atlas 人生副驾管理后台",
    "SITE_URL": "/",
    "SITE_ICON": None,
    "SITE_LOGO": None,
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]
