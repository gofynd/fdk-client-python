"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ValidatePincodeSchema(BaseSchema):
    # Logistic swagger.json

    
    journey = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    

