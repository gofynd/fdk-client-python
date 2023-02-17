"""rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ConfigurationRes(BaseSchema):
    #  swagger.json

    
    valid_android_packages = fields.List(fields.Str(required=False), required=False)
    
    terms_conditions_link = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
