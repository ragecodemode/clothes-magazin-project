from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.categories import Category as CategoryEntity
from core.apps.products.entities.products import Product as ProductEntity


class Category(TimedBaseModel):
    """Категория товаров."""
    title = models.CharField(
        verbose_name='Название категории',
        unique=True,
        max_length=50
    )
    product = models.ForeignKey(
        to='products.Product',
        verose_name='Product',
        related_name='products_categories',
        on_delete=models.CASCADE
    )
    
    @classmethod
    def from_entity(
        cls,
        product: ProductEntity,
    ) -> 'Category':
        return cls(
            id=product.id,
            title=product.title,
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
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
