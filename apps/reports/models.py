from django.db import models


class LifeReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    assessment_id = models.BigIntegerField()
    title = models.CharField(max_length=128)
    status = models.CharField(max_length=32)
    markdown_content = models.TextField(null=True, blank=True)
    content_json = models.JSONField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "life_reports"
        verbose_name = "AI报告"
        verbose_name_plural = "AI报告"

    def __str__(self) -> str:
        return self.title
