from django.db import models

from core.apps.common.models import TimedBaseModel


class Product(TimedBaseModel):
    """Модель для товаров."""
    titile = models.CharField(
        verbose_name='Название продукта',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание продукта',
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='Автивен ли товар',
        default=True,
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'