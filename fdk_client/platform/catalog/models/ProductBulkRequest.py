"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ProductTemplate import ProductTemplate









from .UserDetail1 import UserDetail1





















from .UserDetail1 import UserDetail1



class ProductBulkRequest(BaseSchema):
    #  swagger.json

    
    created_on = fields.Str(required=False)
    
    template = fields.Nested(ProductTemplate, required=False)
    
    total = fields.Int(required=False)
    
    succeed = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserDetail1, required=False)
    
    stage = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    cancelled = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    file_path = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    failed = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    modified_by = fields.Nested(UserDetail1, required=False)
    
