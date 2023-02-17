"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .InventoryExportQuantityFilter import InventoryExportQuantityFilter







class InventoryExportFilter(BaseSchema):
    #  swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    quantity = fields.Nested(InventoryExportQuantityFilter, required=False)
    
    to_date = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
