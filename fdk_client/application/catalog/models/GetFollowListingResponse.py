"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Page import Page



from .ProductListingDetail import ProductListingDetail



class GetFollowListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    