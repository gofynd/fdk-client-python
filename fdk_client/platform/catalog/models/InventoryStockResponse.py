"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .InventoryPage import InventoryPage



class InventoryStockResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(InventoryPage, required=False)
    
