"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSortOn import ProductSortOn

from .Page import Page

from .ProductFilters import ProductFilters



from .ProductListingDetail import ProductListingDetail


class ApplicationProductListingResponse(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    operators = fields.Dict(required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    

