"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .UserDetail1 import UserDetail1

















from .UserDetail1 import UserDetail1







from .ProductTemplate import ProductTemplate







class ProductBulkRequest(BaseSchema):
    #  swagger.json

    
    failed = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    modified_by = fields.Nested(UserDetail1, required=False)
    
    company_id = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    succeed = fields.Int(required=False)
    
    created_by = fields.Nested(UserDetail1, required=False)
    
    cancelled = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    template = fields.Nested(ProductTemplate, required=False)
    
    created_on = fields.Str(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    