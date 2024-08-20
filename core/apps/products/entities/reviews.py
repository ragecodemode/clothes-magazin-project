from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime

from core.apps.common.enums import EntityStatus
from core.apps.customers.entities.customers import Customer
from core.apps.products.entities.products import Product
from core.apps.common.constants import RATING


@dataclass
class Review:
    id: int | None = field(default=None, kw_only=True)  # noqa
    customer: Customer | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str | None = field(default=None)
    rating: int = field(default=RATING)
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime | None = field(default=None)