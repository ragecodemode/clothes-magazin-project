from datetime import datetime

from pydantic import BaseModel

from core.apps.products.entities.products import Product as ProductEntity

class ProductSchema(BaseModel):
    id: int
    title: str
    discription: str
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
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

ProductListSchema = list[ProductSchema]