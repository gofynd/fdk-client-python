"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class InventoryExportRequest(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    brand = fields.List(fields.Int(required=False), required=False)
    
    store = fields.List(fields.Int(required=False), required=False)
    
