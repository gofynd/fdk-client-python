"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class InventoryExportRequest(BaseSchema):
    #  swagger.json

    
    store = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    
    brand = fields.List(fields.Int(required=False), required=False)
    
