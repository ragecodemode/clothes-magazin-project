from datetime import datetime

from pydantic import BaseModel

from core.apps.products.entities.products import Product as ProductEntity

class ProductSchema(BaseModel):
    id: int
    title: str
    discription: str
    price: int
    size: list[str]
    created_at: datetime
    updated_at: datetime | None = None
    
    @classmethod
    def from_entity(cls, product: ProductEntity) -> 'ProductSchema':
        return cls(
            id=product.id,
            title=product.title,
            discription=product.discription,
            price=product.price,
            size=product.size,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )
