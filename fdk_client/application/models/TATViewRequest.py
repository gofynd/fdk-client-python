"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .LocationDetails import LocationDetails




class TATViewRequest(BaseSchema):
    # Logistic swagger.json

    
    journey = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(LocationDetails, required=False), required=False)
    
    action = fields.Str(required=False)
    

