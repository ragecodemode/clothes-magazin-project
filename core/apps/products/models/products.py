from django.core.validators import MinValueValidator
from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.common.constants import PRICE, SIZES
from core.apps.products.entities.products import Product as ProductEntity


class Product(TimedBaseModel):
    """Модель для товаров."""
    title = models.CharField(
        verbose_name='Название продукта',
        max_length=255,
    )
    discription = models.TextField(
        verbose_name='Описание продукта',
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='Автивен ли товар',
        default=True,
    )
    price = models.IntegerField(
        verbose_name='Цена',
        validators=(MinValueValidator(PRICE),),
        error_messages={"errors": "Цена не может быть отрицательной!"},
        default=PRICE,
    )
    size = models.CharField(
        verbose_name='Размер',
        max_length=1,
        choices=SIZES
    )
    
    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            discription=self.discription,
            price=self.price,
            size=self.size,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'