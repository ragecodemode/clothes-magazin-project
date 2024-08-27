from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities.favorites import Favorite as FavoriteEntity

class Favorite(TimedBaseModel):
    """Модель для избранных товаров."""
    customer = models.ForeignKey(
        to='customers.Customer',
        verbose_name='Customer',
        related_name='cutomer_favorite',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to='products.Product',
        verbose_name='Product',
        related_name='product_favorite',
        on_delete=models.CASCADE,
    )
    
    def to_entity(self) -> FavoriteEntity:
        return FavoriteEntity(
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Избранный товар'
        verbose_name_plural = 'Избранные товары'
        unique_together = (
            ('customer', 'product'),
        )