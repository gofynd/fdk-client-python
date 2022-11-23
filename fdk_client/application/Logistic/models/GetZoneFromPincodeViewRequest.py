"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetZoneFromPincodeViewRequest(BaseSchema):
    #  swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
