"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetZoneFromPincodeViewResponse(BaseSchema):
    #  swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    
