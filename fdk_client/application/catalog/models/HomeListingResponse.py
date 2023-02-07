"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductListingDetail import ProductListingDetail



from .Page import Page



class HomeListingResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
