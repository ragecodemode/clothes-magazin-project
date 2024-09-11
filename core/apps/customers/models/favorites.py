from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities.favorites import Favorite as FavoriteEntity
from core.apps.products.entities.products import Product as ProductEntity
from core.apps.customers.entities.customers import Customer as CustomerEntity

class Favorite(TimedBaseModel):
    """Модель для избранных товаров."""
    customer = models.ForeignKey(
        to='customers.Customer',
        verbose_name='Customer',
        related_name='product_favorite',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to='products.Product',
        verbose_name='Product',
        related_name='product_favorite',
        on_delete=models.CASCADE,
    )
    
    @classmethod
    def from_entity(
        cls,
        product: ProductEntity,
        customer: CustomerEntity
    ) -> 'Favorite':
        return cls(
            product=product.id,
            cutomer=customer.id,
        )
    
    def to_entity(self) -> FavoriteEntity:
        return FavoriteEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        unique_together = (
            ('customer', 'product'),
        )