from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.common.constants import RATING
from core.apps.products.entities.reviews import Review as ReviewEntity
from core.apps.products.entities.products import Product as ProductEntity
from core.apps.customers.entities.customers import Customer as CustomerEntity


class Review(TimedBaseModel):
    """Модель для отзывов."""
    customer = models.ForeignKey(
        to='customers.Customer',
        verbose_name='Reviewer',
        related_name='product_reviews',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to='products.Product',
        verbose_name='Product',
        related_name='product_reviews',
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        default=RATING,
    )
    text = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        default='',
    )

    @classmethod
    def from_entity(
        cls,
        review: ReviewEntity,
        product: ProductEntity,
        customer: CustomerEntity
        ) -> 'Review':
        return cls(
            product=product.id,
            customer=customer.id,
            rating=review.rating,
            text=review.text,
        )
    
    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            id=self.id,
            rating=self.rating,
            comment=self.text,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        unique_together = (
            ('customer', 'product'),
        )
       