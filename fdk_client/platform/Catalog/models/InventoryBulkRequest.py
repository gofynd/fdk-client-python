"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .InventoryJobPayload import InventoryJobPayload







class InventoryBulkRequest(BaseSchema):
    #  swagger.json

    
    company_id = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(InventoryJobPayload, required=False), required=False)
    
    batch_id = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
