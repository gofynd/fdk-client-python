"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InternalErrorResponseGenerateBulk(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    error_message = fields.Str(required=False)
    

