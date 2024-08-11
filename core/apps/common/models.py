from django.db import models

class TimedBaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Дата создание',
        auto_now_add=True,
    )
    updated_ad = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    
    class Meta:
        abstract = True