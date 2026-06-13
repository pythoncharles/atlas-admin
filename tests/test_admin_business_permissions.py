from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User as DjangoUser
from django.test import RequestFactory

from apps.users.models import User
from common.business_admin import BusinessModelAdmin


def test_business_admin_keeps_default_operation_permissions() -> None:
    request = RequestFactory().get("/admin/")
    request.user = DjangoUser(is_staff=True, is_superuser=True)
    model_admin = BusinessModelAdmin(User, AdminSite())

    assert model_admin.has_add_permission(request) is True
    assert model_admin.has_change_permission(request) is True
    assert model_admin.has_delete_permission(request) is True
    assert model_admin.get_readonly_fields(request) == ()
