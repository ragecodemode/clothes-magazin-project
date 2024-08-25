from abc import (
    ABC,
    abstractmethod,
)
from django.db import Q

from typing import Iterable

from core.api.filters import PaginationIn
from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductModel
from core.api.v1.products.filters import ProductFilters


class BaseProductService(ABC):
    
    @abstractmethod
    def get_product_list(self, ProductFilters, pagination: PaginationIn) -> Iterable[Product]:
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
    def get_product_in_category(self) -> Iterable[Product]:
        ...

class ORMProductServie(BaseProductService):
    
    def __build_product_query(self, filters: ProductFilters) -> Q:
        query = Q(is_active=True)
        
        if filters is not None:
            query &= Q(title__icontains=filters.search) | Q(description_icontains=filters.search)
            
        return query
    
    def get_product_list(self, filters: ProductFilters, pagination: PaginationIn) -> Iterable[Product]:
        query = self.__build_product_query(filter)
        
        qs = ProductModel.objects.filter(query)[pagination.offset:pagination.offset + pagination.limit]
        
        return [product.to_entity() for product in qs]
    
    def get_product_count(self, filters: ProductFilters) -> int:
        query = self.__build_product_query(filter)
        
        return ProductModel.objects.filter(query).count()
    
    def get_all_product(self) -> Iterable[Product]:
        ...

    def get_product_by_id(self, product_id: int) -> int:
        ...
    
    def get_product_in_category(self) -> Iterable[Product]:
        ...