from django.contrib import admin

from apps.shares.models import ShareRecord
from common.business_admin import BusinessModelAdmin


@admin.register(ShareRecord)
class ShareRecordAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "biz_type", "biz_id", "channel", "share_token", "created_at")
    search_fields = ("user_id", "biz_type", "share_token")
    list_filter = ("biz_type", "channel", "created_at")
