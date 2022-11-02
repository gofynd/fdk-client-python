"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .InventoryJobPayload import InventoryJobPayload







class InventoryBulkRequest(BaseSchema):
    #  swagger.json

    
    batch_id = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(InventoryJobPayload, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    user = fields.Dict(required=False)
    
