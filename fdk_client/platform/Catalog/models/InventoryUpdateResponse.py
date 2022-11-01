"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InventoryResponseItem import InventoryResponseItem





class InventoryUpdateResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(InventoryResponseItem, required=False), required=False)
    
    message = fields.Str(required=False)
    
