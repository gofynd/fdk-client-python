"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .InventoryResponseItem import InventoryResponseItem



class InventoryUpdateResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(InventoryResponseItem, required=False), required=False)
    
