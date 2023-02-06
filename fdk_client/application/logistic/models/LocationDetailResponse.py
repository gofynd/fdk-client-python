"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class LocationDetailResponse(BaseSchema):
    #  swagger.json

    
    longitude = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
