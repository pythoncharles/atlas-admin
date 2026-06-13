from django.db import models


class AssessmentQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    dimension = models.CharField(max_length=64)
    question_type = models.CharField(max_length=32)
    options_json = models.JSONField(null=True, blank=True)
    sort_order = models.IntegerField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "assessment_questions"
        verbose_name = "问卷题目"
        verbose_name_plural = "问卷题目"

    def __str__(self) -> str:
        return self.title


class AssessmentAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    assessment_id = models.BigIntegerField()
    question_id = models.BigIntegerField()
    answer_json = models.JSONField()
    score = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "assessment_answers"
        verbose_name = "问卷回答"
        verbose_name_plural = "问卷回答"


class LifeAssessment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    status = models.CharField(max_length=32)
    total_score = models.IntegerField(null=True, blank=True)
    dimension_scores_json = models.JSONField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "life_assessments"
        verbose_name = "体检记录"
        verbose_name_plural = "体检记录"
