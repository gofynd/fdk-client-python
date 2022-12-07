"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CreateOrderConifgErrorResponse(BaseSchema):
    # Order swagger.json

    
    error = fields.Str(required=False)
    

