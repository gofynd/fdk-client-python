"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AppInventoryStores import AppInventoryStores



from .Page import Page



class StoresResponse(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(AppInventoryStores, required=False)
    
    page = fields.Nested(Page, required=False)
    
