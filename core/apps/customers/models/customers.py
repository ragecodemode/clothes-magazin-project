from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities.customers import Customer


class Customer(TimedBaseModel):
    """Модель для пользователей."""
    name = models.CharField(
        verbose_name='Name',
        max_length=15,
        blank=False,
    )
    email = models.CharField(
        verbose_name='Email',
        max_length=25,
        unique=True,
        blank=False,
    )
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=20,
        unique=True,
    )
    token = models.CharField(
        verbose_name='User Token',
        max_length=255,
        default=uuid4,
        unique=True,
    )

    def __str__(self) -> str:
        return self.phone

    def to_entity(self) -> Customer:
        return Customer(
            id=self.id,
            name=self.name,
            phone=self.phone,
            email=self.email,
            created_at=self.created_at,
        )

    class Meta:
        ordering= ('id')
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'