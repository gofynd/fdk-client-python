"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .TATLocationDetailsRequest import TATLocationDetailsRequest






class TATViewRequest(BaseSchema):
    # Logistic swagger.json

    
    identifier = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsRequest, required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    
    action = fields.Str(required=False)
    

