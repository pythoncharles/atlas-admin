from django.db import models


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_no = models.CharField(max_length=64)
    product_type = models.CharField(max_length=32)
    product_id = models.CharField(max_length=64, null=True, blank=True)
    duration_days = models.IntegerField(default=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=32)
    payment_channel = models.CharField(max_length=32, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "orders"
        verbose_name = "订单"
        verbose_name_plural = "订单"


class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    plan_code = models.CharField(max_length=64)
    status = models.CharField(max_length=32)
    starts_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    source_order_no = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "subscriptions"
        verbose_name = "会员"
        verbose_name_plural = "会员"
