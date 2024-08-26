from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException
from core.apps.products.entities.categories import Category


@dataclass(eq=False)
class CategoryNotFound(ServiceException):
    product_id: int

    @property
    def message(self):
        return 'Category not found'