"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class InventoryExportResponse(BaseSchema):
    #  swagger.json

    
    trigger_on = fields.Str(required=False)
    
    request_params = fields.Dict(required=False)
    
    task_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
