"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ConfigurationBucketPoints(BaseSchema):
    #  swagger.json

    
    start = fields.Float(required=False)
    
    display = fields.Str(required=False)
    
    end = fields.Float(required=False)
    
