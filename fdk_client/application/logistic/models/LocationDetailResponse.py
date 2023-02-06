"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class LocationDetailResponse(BaseSchema):
    #  swagger.json

    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
