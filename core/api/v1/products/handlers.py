from django.http import HttpRequest
from ninja import (
    Router, 
    Query,
)

from core.api.filters import PaginationIn, PaginationOut
from core.api.schemas import ApiResponse, ListPaginatedResponse

from core.apps.products.services.products import BaseProductService, ORMProductServie
from core.apps.products.services.categories import BaseCategoryService, ORMCategoryService
from core.api.v1.products.schemas import ProductSchema, CategorySchema
from core.api.v1.products.filters import CategoryFilters, ProductFilters

router = Router(tags=['Products'])
router = Router(tags=['Category'])

@router.get('/products', response=ApiResponse[ListPaginatedResponse[ProductSchema]])
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

@router.get('/category', response=ApiResponse[ListPaginatedResponse[CategorySchema]])
def get_category_list_handler(
    request: HttpRequest,
    filters: Query[CategoryFilters],
    pagination_in: Query[PaginationIn]
) -> ApiResponse[ListPaginatedResponse[CategorySchema]]:
    service: BaseCategoryService = ORMCategoryService()
    
    category_list = service.get_category_list(filters=filters, pagination=pagination_in)
    category_count = service.get_category_count(filters=filters)
    
    items = [CategorySchema.from_entity(obj) for obj in category_list]
    
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=category_count
    )
    
    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out)
    )