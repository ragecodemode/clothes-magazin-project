from django.db.models import models

from core.apps.common.models import TimedBaseModel
from core.apps.common.constants import RATING
from core.apps.products.entities.reviews import Review as ReviewEntity


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
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        default='',
    )
    
    # TODO: доделать from_entity
    @classmethod
    def from_entity():
        pass
    
    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            id=self.id,
            rating=self.rating,
            comment=self.comment,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = (
            ('customer', 'product'),
        )
       