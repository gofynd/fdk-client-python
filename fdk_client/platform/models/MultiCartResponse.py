"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CartList import CartList




class MultiCartResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.List(fields.Nested(CartList, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

