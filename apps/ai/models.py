from django.db import models


class PromptTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=32)
    system_prompt = models.TextField()
    user_prompt = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "prompt_templates"
        verbose_name = "Prompt模板"
        verbose_name_plural = "Prompt模板"


class AiCallLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(null=True, blank=True)
    biz_type = models.CharField(max_length=64)
    model_provider = models.CharField(max_length=32)
    model_name = models.CharField(max_length=64)
    prompt_code = models.CharField(max_length=64, null=True, blank=True)
    prompt_version = models.CharField(max_length=32, null=True, blank=True)
    request_payload_json = models.JSONField(null=True, blank=True)
    response_payload_json = models.JSONField(null=True, blank=True)
    input_tokens = models.BigIntegerField()
    output_tokens = models.BigIntegerField()
    cost_amount = models.DecimalField(max_digits=12, decimal_places=6)
    status = models.CharField(max_length=32)
    error_message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "ai_call_logs"
        verbose_name = "AI调用日志"
        verbose_name_plural = "AI调用日志"
