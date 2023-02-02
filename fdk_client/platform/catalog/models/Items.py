"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























from .UserCommon import UserCommon





from .UserCommon import UserCommon







class Items(BaseSchema):
    #  swagger.json

    
    retry = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    tracking_url = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserCommon, required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserCommon, required=False)
    
    cancelled = fields.Int(required=False)
    
    succeed = fields.Int(required=False)
    
