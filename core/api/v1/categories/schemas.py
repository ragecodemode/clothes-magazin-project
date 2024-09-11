from datetime import datetime

from pydantic import BaseModel

from core.apps.products.entities.categories import Category as CategoryEntity

class CategoriInSchema(BaseModel):
    title: str
    
    def to_entity(self):
        return CategoryEntity(title=self.title)


class CategorySchema(BaseModel):
    product_id: int
    category: CategoriInSchema


class CategoryOutSchema(CategoriInSchema):
    id: int  # noqa
    created_at: datetime
    updated_at: datetime | None
    
    @classmethod
    def from_entity(cls, category: CategoryEntity) -> 'CategoryOutSchema':
        return cls(
            id=category.id,
            title=category.title,
            created_at=category.created_at,
            updated_at=category.updated_at,
        )
