from django.contrib import admin

from apps.weekly.models import WeeklyReview
from common.business_admin import BusinessModelAdmin


@admin.register(WeeklyReview)
class WeeklyReviewAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "week_start", "week_end", "title", "created_at")
    search_fields = ("title", "content", "user_id")
    list_filter = ("week_start", "week_end", "created_at")
