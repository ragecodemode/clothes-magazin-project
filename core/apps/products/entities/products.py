from dataclasses import (
    dataclass,
    field
)
from datetime import datetime

from core.apps.common.constants import PRICE
from core.apps.products.exceptions.products import InvalidProduct

@dataclass
class Product:
    id: int # noqa
    title: str
    discription: str
    price: int = field(default=PRICE)
    size: list[str] = field(default_factory=list)
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime | None = field(default=None)
    
    def __post__init__(self):
        if not isinstance(self.title, str) and self.title in '@!#$%^&*()':
            raise InvalidProduct('Invalid product title')

        if not isinstance(self.discription, str) and len(self.discription) > 250:
            raise InvalidProduct('Invalid product description')