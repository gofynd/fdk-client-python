"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetProductBundleCreateResponse import GetProductBundleCreateResponse



from .Page import Page



class GetProductBundleListingResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(GetProductBundleCreateResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
