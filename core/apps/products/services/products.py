from abc import (
    ABC,
    abstractmethod,
)
from typing import Iterable

from core.apps.products.entities.products import Product
from core.apps.products.models.products import Product as ProductModel


class BaseProductService(ABC):
    
    @abstractmethod
    def get_product_list(self) -> Iterable[Product]:
        ...
    
    @abstractmethod
    def get_product_count(self) -> int:
        ...


class ORMProductServie(BaseProductService):
    
    def get_product_list(self) -> Iterable[Product]:
        qs = ProductModel.objects.filter(is_active=True)
        
        return [product.to_entity() for product in qs]
    
    def get_product_count(self) -> int:
        return ProductModel.objects.filter(is_active=True).count()