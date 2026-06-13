from django.contrib import admin
from unfold.admin import ModelAdmin


class BusinessModelAdmin(ModelAdmin):
    pass


def register_business_model(model, admin_class: type[BusinessModelAdmin] | None = None) -> None:
    admin.site.register(model, admin_class or BusinessModelAdmin)
