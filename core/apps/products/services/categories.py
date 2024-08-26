from abc import (
    ABC,
    abstractmethod,
)

from typing import Iterable

from core.apps.products.entities.categories import Category
from core.apps.products.exceptions.categories import CategoryNotFound
from core.apps.products.models.categories import Category as CategoryModel
from core.api.v1.products.filters import CategoryFilters
from core.api.filters import PaginationIn

class BaseCategoryService(ABC):
    
    @abstractmethod
    def get_category_list(
        self,
        filters: CategoryFilters,
    ) -> Iterable[Category]:
        ...
    
    @abstractmethod
    def get_category_count(self, filters: CategoryFilters) -> Iterable[Category]:
        ...
    
    @abstractmethod
    def get_category_by_id(self, category_id: int) -> int:
        ...
    
    @abstractmethod
    def get_all_category(self) -> Iterable[Category]:
        ...


class ORMCategoryService(BaseCategoryService):
    
    def get_category_list(
        self,
        filters: CategoryFilters,
    ) -> Iterable[Category]:
        qs = CategoryModel.objects.filter(filters)
        
        return [category.to_entity() for category in qs]
    
    def get_category_count(self, filters: CategoryFilters) -> Iterable[Category]:
        
        return CategoryModel.objects.all(filters).count()
    
    def get_category_by_id(self, category_id: int) -> int:
        try:
            categroy_dto = CategoryModel.objects.get(id=category_id)
        except CategoryModel.DoesNotExist:
            raise CategoryNotFound(category_id=category_id)
        
        return categroy_dto.to_entity()
    
    def get_all_category(self) -> Iterable[Category]:
        return CategoryModel.objects.all()