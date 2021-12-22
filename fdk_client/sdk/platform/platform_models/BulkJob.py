"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



























from .UserInfo1 import UserInfo1



from .UserInfo1 import UserInfo1




class BulkJob(BaseSchema):
    # Catalog swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    cancelled = fields.Int(required=False)
    
    custom_template_tag = fields.Str(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    succeed = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Dict(required=False), required=False)
    
    tracking_url = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo1, required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserInfo1, required=False)
    
    failed = fields.Int(required=False)
    

