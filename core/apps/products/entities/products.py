from dataclasses import (
    dataclass,
    field
)
from datetime import datetime

from core.apps.common.constants import PRICE, SIZES

@dataclass
class Product:
    id: int # noqa
    title: str
    discription: str
    price: int = field(default=PRICE)
    size: str = field(default=SIZES)
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime