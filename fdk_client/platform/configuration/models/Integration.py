"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Validators import Validators

















from .IntegrationMeta import IntegrationMeta

















class Integration(BaseSchema):
    #  swagger.json

    
    validators = fields.Nested(Validators, required=False)
    
    description = fields.Str(required=False)
    
    description_html = fields.Str(required=False)
    
    constants = fields.Dict(required=False)
    
    companies = fields.List(fields.Dict(required=False), required=False)
    
    support = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.List(fields.Nested(IntegrationMeta, required=False), required=False)
    
    icon = fields.Str(required=False)
    
    owner = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
