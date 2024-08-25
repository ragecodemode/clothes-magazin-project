from dataclasses import (
    dataclass,
    field
)
from datetime import datetime

from core.apps.common.constants import PRICE, SIZES
from core.apps.common.enums import EntityStatus
from core.apps.products.entities.categoris import Category
from core.apps.products.exceptions.products import InvalidProduct

@dataclass
class Product:
    id: int # noqa
    title: str
    discription: str
    price: int = field(default=PRICE)
    size: list[str] = field(default_factory=list, default=SIZES)
    category: Category | EntityStatus = field(default_factory=EntityStatus.NOT_LOADED)
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime
    
    def __post__init__(self):
        if not isinstance(self.title, str) and self.title in '@!#$%^&*()':
            raise InvalidProduct('Invalid product title')

        if not isinstance(self.discription, str) and len(self.discription) > 250:
            raise InvalidProduct('Invalid product description')