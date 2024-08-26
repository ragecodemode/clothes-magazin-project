from dataclasses import (dataclass, field)

from datetime import datetime

@dataclass
class Category:
    id: int # noqa
    title: str
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    updated_at: datetime | None = field(default=None)