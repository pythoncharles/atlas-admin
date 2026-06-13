from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    openid = models.CharField(max_length=128)
    unionid = models.CharField(max_length=128, null=True, blank=True)
    nickname = models.CharField(max_length=64, null=True, blank=True)
    avatar_url = models.CharField(max_length=512, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    status = models.CharField(max_length=32)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "users"
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self) -> str:
        return self.nickname or self.openid


class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    gender = models.CharField(max_length=32, null=True, blank=True)
    age_range = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    occupation = models.CharField(max_length=128, null=True, blank=True)
    education = models.CharField(max_length=64, null=True, blank=True)
    life_stage = models.CharField(max_length=64, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "user_profiles"
        verbose_name = "用户画像"
        verbose_name_plural = "用户画像"
