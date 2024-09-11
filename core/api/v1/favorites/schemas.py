from datetime import datetime

from pydantic import BaseModel

from core.apps.customers.entities.favorites import Favorite as FavoriteEntity

class CreateFavoriteSchema(BaseModel):
    product_id: int
    customer_token: str

class FavoriteSchema(BaseModel):
    id : int # noqa
    created_at: datetime
    updated_at: datetime | None
    
    @classmethod
    def from_entity(cls, favorite: FavoriteEntity) -> 'FavoriteSchema':
        return cls(
            id=favorite.id,
            created_at=favorite.created_at,
            updated_at=favorite.updated_at,
        )