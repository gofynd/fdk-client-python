"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductFilters import ProductFilters



from .Page import Page



from .ProductSortOn import ProductSortOn



from .ProductListingDetail import ProductListingDetail



class ProductListingResponse(BaseSchema):
    #  swagger.json

    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
