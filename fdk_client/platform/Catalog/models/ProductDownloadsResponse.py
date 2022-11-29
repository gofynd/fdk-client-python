"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductDownloadsItems import ProductDownloadsItems



from .Page import Page



class ProductDownloadsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(ProductDownloadsItems, required=False)
    
    page = fields.Nested(Page, required=False)
    
