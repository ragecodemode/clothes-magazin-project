from abc import (
    ABC,
    abstractmethod,
)
from django.db.models import Q

from typing import Iterable

from core.api.filters import PaginationIn
from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductModel
from core.api.v1.products.filters import CategoryFilters, ProductFilters


class BaseProductService(ABC):
    
    @abstractmethod
    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn
    ) -> Iterable[Product]:
        ...
    
    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int:
        ...

    @abstractmethod
    def get_all_prodcut(self) -> Iterable[Product]:
        ...

    @abstractmethod
    def get_prodcut_by_id(self, product_id: int) -> int:
        ...
    
    @abstractmethod
    def get_product_in_category(
        self,
        filters: CategoryFilters,
        pagination: PaginationIn
    ) -> Iterable[Product]:
        ...

class ORMProductServie(BaseProductService):
    
    def __build_product_query(self, filters: ProductFilters) -> Q:
        query = Q(is_active=True)
        
        if filters is not None:
            query &= Q(title__icontains=filters.search) | Q(description_icontains=filters.search)
            
        return query
    
    def __build_category_product_query(self, filters: CategoryFilters) -> Q:
        
        if filters is not None:
            query &= Q(title__icontains=filters.search)
            
        return query
    
    def get_product_list(
        self,
        filters: ProductFilters,
        pagination: PaginationIn
    ) -> Iterable[Product]:
        query = self.__build_product_query(filters)
        
        qs = ProductModel.objects.filter(query)[pagination.offset:pagination.offset + pagination.limit]
        
        return [product.to_entity() for product in qs]
    
    def get_product_count(self, filters: ProductFilters) -> int:
        query = self.__build_product_query(filters)
        
        return ProductModel.objects.filter(query).count()
    
    def get_all_product(self) -> Iterable[Product]:
        ...

    def get_product_by_id(self, product_id: int) -> int:
        ...
    
    def get_product_in_category(
        self,
        filters: CategoryFilters,
        pagination: PaginationIn
    ) -> Iterable[Product]:
        query = self.__build_category_product_query(filters)
        
        qs = ProductModel.objects.filter(query)[pagination.offset:pagination.offset + pagination.limit]
        
        return [product_category.to_entity() for product_category in qs]