from django.db import models


class WeeklyReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    week_start = models.DateField()
    week_end = models.DateField()
    title = models.CharField(max_length=128)
    content = models.TextField()
    metrics_json = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "weekly_reviews"
        verbose_name = "周报复盘"
        verbose_name_plural = "周报复盘"

    def __str__(self) -> str:
        return self.title
