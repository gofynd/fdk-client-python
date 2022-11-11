"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InventoryResponse import InventoryResponse



from .Page import Page



class InventoryResponsePaginated(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(InventoryResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
