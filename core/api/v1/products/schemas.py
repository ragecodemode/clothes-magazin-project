from datetime import datetime

from pydantic import BaseModel

from core.apps.products.entities.products import Product as ProductEntity
from core.apps.products.entities.categories import Category as CategoryEntity

class ProductSchema(BaseModel):
    id: int
    title: str
    discription: str
    category: CategoryEntity
    created_at: datetime
    updated_at: datetime
    
    @staticmethod
    def from_entity(entity: ProductEntity) -> 'ProductSchema':
        return ProductSchema(
            id=entity.id,
            title=entity.title,
            discription=entity.discription,
            size=entity.size,
            price=entity.price,
            category=entity.category,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


class CategorySchema(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    
    @staticmethod
    def from_entity(entity: CategoryEntity) -> 'CategorySchema':
        return CategorySchema(
            id=entity.id,
            title=entity.title,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )