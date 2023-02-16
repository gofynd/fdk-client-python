"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .InventoryExportAdvanceOption import InventoryExportAdvanceOption











class InventoryExportJob(BaseSchema):
    #  swagger.json

    
    completed_on = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    request_params = fields.Nested(InventoryExportAdvanceOption, required=False)
    
    trigger_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    url = fields.Str(required=False)
    
