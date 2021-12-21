"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ProductListingDetail import ProductListingDetail

from .Page import Page

from .ProductSortOn import ProductSortOn

from .ProductFilters import ProductFilters


class GetCollectionItemsResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    

