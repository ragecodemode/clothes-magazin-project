from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.categories import Category as CategoryEntity


class Category(TimedBaseModel):
    """Категория товаров."""
    title = models.CharField(
        verbose_name='Название категории',
        unique=True,
        max_length=50
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
