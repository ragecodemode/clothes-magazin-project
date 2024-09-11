from django.http import HttpRequest
from ninja import (
    Router, 
    Query,
)

from core.api.filters import PaginationIn, PaginationOut
from core.api.schemas import ApiResponse, ListPaginatedResponse

from core.apps.products.services.products import BaseProductService, ORMProductServie
from core.api.v1.products.schemas import ProductSchema
from core.api.v1.products.filters import ProductFilters

router = Router(tags=['Products'])

@router.get('/products_list', response=ApiResponse[ListPaginatedResponse[ProductSchema]])
def get_product_list_handler(
    request: HttpRequest,
    filters: Query[ProductFilters],
    pagination_in: Query[PaginationIn]
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    service: BaseProductService = ORMProductServie()
    product_list = service.get_product_list(filters=filters, pagination=pagination_in)
    product_count = service.get_product_count(filters=filters)

    items = [ProductSchema.from_entity(obj) for obj in product_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=product_count
    )
    
    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out)
    )

@router.get('/products_by_id', response=ApiResponse[ListPaginatedResponse[ProductSchema]])
def get_products_by_id(
    request: HttpRequest,
    product_id: int,
    filters: Query[ProductFilters],
    pagination_in: Query[PaginationIn]
) -> ApiResponse[ListPaginatedResponse[ProductSchema]]:
    service: BaseProductService = ORMProductServie()
    
    product_by_id = service.get_produсt_by_id(product_id)
    product_count = service.get_product_count(filters=filters)

    items = [ProductSchema.from_entity(obj) for obj in product_by_id if obj == obj.id]

    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=product_count
    )
    
    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out)
    )