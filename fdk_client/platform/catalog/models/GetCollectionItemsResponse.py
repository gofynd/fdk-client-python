"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductSortOn import ProductSortOn



from .Page import Page



from .ProductListingDetail import ProductListingDetail



from .ProductFilters import ProductFilters



class GetCollectionItemsResponse(BaseSchema):
    #  swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
