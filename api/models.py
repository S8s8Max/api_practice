from django.db import models

# Create your models here.
class Log(models.Model):
    created_at = models.DateTimeField(
        verbose_name="登録時間",
        auto_now_add=True,
    )
    country = models.TextField(
        verbose_name="国",
        max_length=100,
    )
    interest_rate = models.FloatField(
        verbose_name="利子率",
        blank=True,
    )
    def __str__(self):
        return self.created_at

    class Meta:
        verbose_name = '採取データ'
        verbose_name_plural = '採取データ'
