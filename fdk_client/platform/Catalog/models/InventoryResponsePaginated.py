"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .InventoryResponse import InventoryResponse



class InventoryResponsePaginated(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(InventoryResponse, required=False), required=False)
    
