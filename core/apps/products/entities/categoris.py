from dataclasses import (dataclass, field)

from datetime import datetime

from core.apps.common.enums import EntityStatus
from core.apps.products.entities.products import Product

@dataclass
class Category:
    id: int # noqa
    title: str
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime | None = field(default=None)