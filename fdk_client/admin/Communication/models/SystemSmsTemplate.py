"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















from .SmsTemplateMessage import SmsTemplateMessage











class SystemSmsTemplate(BaseSchema):
    #  swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    message = fields.Nested(SmsTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
