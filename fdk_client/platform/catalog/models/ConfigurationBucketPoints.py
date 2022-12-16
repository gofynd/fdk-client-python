"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ConfigurationBucketPoints(BaseSchema):
    #  swagger.json

    
    end = fields.Float(required=False)
    
    start = fields.Float(required=False)
    
    display = fields.Str(required=False)
    