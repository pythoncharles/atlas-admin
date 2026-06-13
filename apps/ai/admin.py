from django.contrib import admin

from apps.ai.models import AiCallLog, PromptTemplate
from common.permissions import mask_text
from common.business_admin import BusinessModelAdmin


@admin.register(PromptTemplate)
class PromptTemplateAdmin(BusinessModelAdmin):
    list_display = ("id", "code", "name", "version", "is_active", "created_at")
    search_fields = ("code", "name", "version")
    list_filter = ("code", "version", "is_active")


@admin.register(AiCallLog)
class AiCallLogAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "biz_type", "model_provider", "model_name", "status", "created_at")
    search_fields = ("user_id", "biz_type", "prompt_code", "error_message")
    list_filter = ("biz_type", "model_provider", "status", "created_at")

    @admin.display(description="request")
    def masked_request_payload(self, obj: AiCallLog) -> str:
        return mask_text(str(obj.request_payload_json), prefix=12, suffix=8)
