from abc import (
    ABC,
    abstractmethod,
)

from typing import Iterable

from core.apps.products.entities.categoris import Category
from core.apps.products.models.categories import Category as CategoryModel

class CategotyBaseService(ABC):
    
    @abstractmethod
    def get_category_list(self) -> Iterable[Category]:
        ...
    
    @abstractmethod
    def get_category_by_id(self, category_id: int) -> int:
        ...
    
    @abstractmethod
    def get_all_category(self) -> Iterable[Category]:
        ...


class ORMCategoryService(CategotyBaseService):
    
    def get_category_list(self) -> Iterable[Category]:
        ...
    
    def get_category_by_id(self, category_id: int) -> int:
        ...
    
    def get_all_category(self) -> Iterable[Category]:
        ...