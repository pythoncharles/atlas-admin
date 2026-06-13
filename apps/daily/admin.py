from django.contrib import admin

from apps.daily.models import DailySuggestion
from common.business_admin import BusinessModelAdmin


@admin.register(DailySuggestion)
class DailySuggestionAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "suggestion_date", "title", "created_at")
    search_fields = ("title", "content", "user_id")
    list_filter = ("suggestion_date", "created_at")
