from django.conf import settings
from django.urls import reverse


def test_django_starts_and_admin_url_resolves() -> None:
    assert reverse("admin:index") == "/admin/"


def test_unfold_is_enabled_before_django_admin() -> None:
    assert "unfold" in settings.INSTALLED_APPS
    assert settings.INSTALLED_APPS.index("unfold") < settings.INSTALLED_APPS.index("django.contrib.admin")


def test_business_migrations_are_disabled() -> None:
    for app_label in [
        "users",
        "assessments",
        "reports",
        "goals",
        "daily",
        "weekly",
        "payments",
        "ai",
        "shares",
        "files",
    ]:
        assert settings.MIGRATION_MODULES[app_label] is None


def test_business_database_alias_is_configured() -> None:
    assert "business" in settings.DATABASES
    assert settings.DATABASE_ROUTERS == ["common.db_router.BusinessDatabaseRouter"]
