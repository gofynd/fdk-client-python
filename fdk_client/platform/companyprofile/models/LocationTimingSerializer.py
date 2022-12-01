"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class LocationTimingSerializer(BaseSchema):
    #  swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    
