"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .GetProductBundleCreateResponse import GetProductBundleCreateResponse



class GetProductBundleListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetProductBundleCreateResponse, required=False), required=False)
    
