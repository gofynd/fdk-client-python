"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductFilters import ProductFilters



from .ProductSortOn import ProductSortOn



from .ProductListingDetail import ProductListingDetail



from .Page import Page



class GetCollectionItemsResponse(BaseSchema):
    #  swagger.json

    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
