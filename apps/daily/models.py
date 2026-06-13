from django.db import models


class DailySuggestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    suggestion_date = models.DateField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    actions_json = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "daily_suggestions"
        verbose_name = "每日建议"
        verbose_name_plural = "每日建议"

    def __str__(self) -> str:
        return self.title
