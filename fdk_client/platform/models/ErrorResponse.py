"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ErrorResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error_trace = fields.Str(required=False)
    

