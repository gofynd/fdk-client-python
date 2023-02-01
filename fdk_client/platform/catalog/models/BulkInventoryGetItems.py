"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


































class BulkInventoryGetItems(BaseSchema):
    #  swagger.json

    
    modified_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    
    file_path = fields.Str(required=False)
    
    succeed = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    total = fields.Int(required=False)
    
    cancelled = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
