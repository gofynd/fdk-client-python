"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .TATLocationDetailsRequest import TATLocationDetailsRequest







class TATViewRequest(BaseSchema):
    #  swagger.json

    
    to_pincode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsRequest, required=False), required=False)
    
    action = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    