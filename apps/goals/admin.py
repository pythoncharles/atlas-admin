from django.contrib import admin

from apps.goals.models import Goal, GoalTask
from common.business_admin import BusinessModelAdmin


@admin.register(Goal)
class GoalAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "title", "status", "priority", "target_date", "created_at")
    search_fields = ("title", "description", "user_id")
    list_filter = ("status", "target_date", "created_at")


@admin.register(GoalTask)
class GoalTaskAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "goal_id", "title", "status", "sort_order", "due_date")
    search_fields = ("title", "description", "user_id", "goal_id")
    list_filter = ("status", "due_date", "created_at")
