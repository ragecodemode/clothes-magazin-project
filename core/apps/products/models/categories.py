from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.categoris import Category as CategoryEntity


class Category(TimedBaseModel):
    """Категория товаров."""
    title = models.CharField(
        verbose_name='Название категории',
        unique=True,
        max_length=50
    )
    product = models.ForeignKey(
        to='products.Product',
        verbose_name='Product',
        related_name='products_categories',
        on_delete=models.CASCADE,
    )
    
    def to_entity(self) -> CategoryEntity:
        return CategoryEntity(
            id=self.id,
            title=self.title,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
