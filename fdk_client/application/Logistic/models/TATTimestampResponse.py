"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class TATTimestampResponse(BaseSchema):
    #  swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    
