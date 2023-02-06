"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .LocationDetailResponse import LocationDetailResponse



class LocationDataResponse(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    location = fields.Nested(LocationDetailResponse, required=False)
    
