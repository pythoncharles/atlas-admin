from django.contrib import admin

from apps.users.models import User, UserProfile
from common.permissions import mask_text
from common.business_admin import BusinessModelAdmin


@admin.register(User)
class UserAdmin(BusinessModelAdmin):
    list_display = ("id", "masked_openid", "nickname", "masked_phone", "status", "is_active", "created_at")
    search_fields = ("openid", "nickname", "phone")
    list_filter = ("status", "is_active", "created_at")

    @admin.display(description="openid")
    def masked_openid(self, obj: User) -> str:
        return mask_text(obj.openid)

    @admin.display(description="phone")
    def masked_phone(self, obj: User) -> str:
        return mask_text(obj.phone, prefix=3, suffix=2)


@admin.register(UserProfile)
class UserProfileAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "city", "occupation", "education", "life_stage", "created_at")
    search_fields = ("user_id", "city", "occupation")
    list_filter = ("city", "life_stage", "created_at")
