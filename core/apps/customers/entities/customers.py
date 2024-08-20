from dataclasses import (
    dataclass,
    field,
)

from core.apps.customers.exceptions.codes import ValidateException

from datetime import datetime
import re


@dataclass
class Customer:
    id: int  # noqa
    name: str
    email: str
    phone: str | None
    created_at: datetime = field(
        default_factory=datetime.now,
        kw_only=True,
    )
    
    def __post_init__(self):
        if not isinstance(self.name, str):
            raise ValidateException('Invalid customer name')
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidateException('Invalid email format')
        
        if not re.match(r"^\\+?[1-9][0-9]{7,14}$", self.phone):
            raise ValidateException('Invalid phone number format')