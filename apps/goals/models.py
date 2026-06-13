from django.db import models


class Goal(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=32)
    priority = models.IntegerField()
    target_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "goals"
        verbose_name = "目标"
        verbose_name_plural = "目标"

    def __str__(self) -> str:
        return self.title


class GoalTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    goal_id = models.BigIntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "goal_tasks"
        verbose_name = "目标任务"
        verbose_name_plural = "目标任务"
