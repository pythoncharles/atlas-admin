from django.contrib import admin

from apps.reports.models import LifeReport
from common.business_admin import BusinessModelAdmin


@admin.register(LifeReport)
class LifeReportAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "assessment_id", "title", "status", "created_at")
    search_fields = ("title", "markdown_content")
    list_filter = ("status", "created_at")
