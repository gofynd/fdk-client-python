"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .EmailProviderReqFrom import EmailProviderReqFrom




















class EmailProvider(BaseSchema):

    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    from_ = fields.List(fields.Nested(EmailProviderReqFrom, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

