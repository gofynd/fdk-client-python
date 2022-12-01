"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BrandStoreInfo import BrandStoreInfo



from .Page import Page



class StoreByBrandsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(BrandStoreInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
