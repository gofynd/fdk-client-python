"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductBulkRequest import ProductBulkRequest



from .Page import Page



class ProductBulkRequestList(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(ProductBulkRequest, required=False)
    
    page = fields.Nested(Page, required=False)
    
