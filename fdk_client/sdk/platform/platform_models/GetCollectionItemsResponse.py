"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ProductFilters import ProductFilters

from .ProductSortOn import ProductSortOn

from .Page import Page

from .ProductListingDetail import ProductListingDetail


class GetCollectionItemsResponse(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    

