from django.db import models


class File(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(null=True, blank=True)
    bucket = models.CharField(max_length=128)
    object_name = models.CharField(max_length=512)
    original_filename = models.CharField(max_length=255, null=True, blank=True)
    content_type = models.CharField(max_length=128, null=True, blank=True)
    size = models.BigIntegerField(null=True, blank=True)
    checksum = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "files"
        verbose_name = "文件"
        verbose_name_plural = "文件"
