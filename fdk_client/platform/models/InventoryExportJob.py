"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class InventoryExportJob(BaseSchema):
    # Catalog swagger.json

    
    request_params = fields.Dict(required=False)
    
    completed_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    task_id = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    trigger_on = fields.Str(required=False)
    

