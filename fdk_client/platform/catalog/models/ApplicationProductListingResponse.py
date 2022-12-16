"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .ProductFilters import ProductFilters



from .ProductListingDetail import ProductListingDetail





from .ProductSortOn import ProductSortOn



class ApplicationProductListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    operators = fields.Dict(required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    