"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
































class BulkInventoryGetItems(BaseSchema):
    # Catalog swagger.json

    
    cancelled = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    succeed = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    created_by = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    failed = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    

