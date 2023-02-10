"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class GeoLocation(BaseSchema):
    #  swagger.json

    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
