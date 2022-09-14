"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ErrorResponse import ErrorResponse














class ValidatePincodeResponseSchema(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(ErrorResponse, required=False)
    
    request_uuid = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    to_pincode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    

