"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ConfigurationBucketPoints import ConfigurationBucketPoints









class ConfigurationListingFilterValue(BaseSchema):
    #  swagger.json

    
    map = fields.Dict(required=False)
    
    sort = fields.Str(required=False)
    
    bucket_points = fields.List(fields.Nested(ConfigurationBucketPoints, required=False), required=False)
    
    value = fields.Str(required=False)
    
    condition = fields.Str(required=False)
    
    map_values = fields.List(fields.Dict(required=False), required=False)
    
