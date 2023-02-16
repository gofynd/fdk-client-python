"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .InventoryExportQuantityFilter import InventoryExportQuantityFilter











class InventoryExportAdvanceOption(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    
    quantity = fields.Nested(InventoryExportQuantityFilter, required=False)
    
    notification = fields.Boolean(required=False)
    
    from_date = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
