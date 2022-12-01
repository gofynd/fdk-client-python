"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ConfigurationSchema(BaseSchema):
    #  swagger.json

    
    sleep_time = fields.Int(required=False)
    
    start_on_launch = fields.Boolean(required=False)
    
    duration = fields.Int(required=False)
    
    slide_direction = fields.Str(required=False)
    
