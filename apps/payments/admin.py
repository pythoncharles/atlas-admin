from django.contrib import admin

from apps.payments.models import Order, Subscription
from common.business_admin import BusinessModelAdmin


@admin.register(Order)
class OrderAdmin(BusinessModelAdmin):
    list_display = (
        "id",
        "user_id",
        "order_no",
        "product_type",
        "product_id",
        "duration_days",
        "amount",
        "status",
        "created_at",
    )
    search_fields = ("order_no", "user_id", "product_id")
    list_filter = ("product_type", "status", "payment_channel", "created_at")


@admin.register(Subscription)
class SubscriptionAdmin(BusinessModelAdmin):
    list_display = ("id", "user_id", "plan_code", "status", "starts_at", "expires_at", "source_order_no")
    search_fields = ("user_id", "plan_code", "source_order_no")
    list_filter = ("plan_code", "status", "starts_at", "expires_at")
