from django.contrib import admin

from apps.assessments.models import AssessmentAnswer, AssessmentQuestion, LifeAssessment
from common.business_admin import BusinessModelAdmin


@admin.register(AssessmentQuestion)
class AssessmentQuestionAdmin(BusinessModelAdmin):
    list_display = ("id", "code", "title", "dimension", "question_type", "sort_order", "is_active")
    search_fields = ("code", "title")
    list_filter = ("dimension", "question_type", "is_active")


@admin.register(AssessmentAnswer)
class AssessmentAnswerAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "assessment_id", "question_id", "score", "created_at")
    search_fields = ("user_id", "assessment_id", "question_id")
    list_filter = ("created_at",)


@admin.register(LifeAssessment)
class LifeAssessmentAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "status", "total_score", "created_at")
    search_fields = ("user_id",)
    list_filter = ("status", "created_at")
