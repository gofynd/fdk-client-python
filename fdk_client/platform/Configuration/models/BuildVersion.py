"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class BuildVersion(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    platform_type = fields.Str(required=False)
    
    build_status = fields.Str(required=False)
    
    version_name = fields.Str(required=False)
    
    version_code = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
