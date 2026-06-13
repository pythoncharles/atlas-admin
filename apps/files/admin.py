from django.contrib import admin

from apps.files.models import File
from common.business_admin import BusinessModelAdmin


@admin.register(File)
class FileAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "bucket", "object_name", "content_type", "size", "created_at")
    search_fields = ("user_id", "object_name", "original_filename", "checksum")
    list_filter = ("bucket", "content_type", "created_at")
