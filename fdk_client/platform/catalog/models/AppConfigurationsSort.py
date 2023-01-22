"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class AppConfigurationsSort(BaseSchema):
    #  swagger.json

    
    priority = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    default_key = fields.Str(required=False)
    