"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .LogisticPincodeData import LogisticPincodeData



class GetPincodeCityResponse(BaseSchema):
    #  swagger.json

    
    request_uuid = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(LogisticPincodeData, required=False), required=False)
    
