"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class AppConfigurationsSort(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    default_key = fields.Str(required=False)
    
