"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SignedFailedResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    

