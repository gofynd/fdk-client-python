"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class InventoryExportQuantityFilter(BaseSchema):
    #  swagger.json

    
    min = fields.Int(required=False)
    
    operators = fields.Str(required=False)
    
    max = fields.Int(required=False)
    
