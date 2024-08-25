from ninja import Schema

from core.api.filters import DefaultFilter

class ProductFilters(Schema):
    search: str | None | DefaultFilter = DefaultFilter.NOT_SET