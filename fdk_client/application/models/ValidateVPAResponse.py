"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ValidateUPI import ValidateUPI




class ValidateVPAResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ValidateUPI, required=False)
    
    success = fields.Boolean(required=False)
    

