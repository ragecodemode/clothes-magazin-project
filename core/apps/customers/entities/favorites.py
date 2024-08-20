from dataclasses import (
    dataclass,
    field,
)

from datetime import datetime

from core.apps.common.enums import EntityStatus
from core.apps.customers.entities.customers import Customer
from core.apps.products.entities.products import Product

@dataclass
class Favorite:
    id : int # noqa
    customer: Customer | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: Product | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime | None = field(default=None)