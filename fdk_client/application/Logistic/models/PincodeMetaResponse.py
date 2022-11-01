"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PincodeMetaResponse(BaseSchema):
    #  swagger.json

    
    internal_zone_id = fields.Int(required=False)
    
    zone = fields.Str(required=False)
    
