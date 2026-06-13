from django.db import models


class ShareRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    biz_type = models.CharField(max_length=64)
    biz_id = models.BigIntegerField()
    channel = models.CharField(max_length=64)
    share_token = models.CharField(max_length=128)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "share_records"
        verbose_name = "分享记录"
        verbose_name_plural = "分享记录"
