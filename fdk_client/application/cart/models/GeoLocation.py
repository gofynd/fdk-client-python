"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GeoLocation(BaseSchema):
    #  swagger.json

    
    longitude = fields.Float(required=False)
    
    latitude = fields.Float(required=False)
    
