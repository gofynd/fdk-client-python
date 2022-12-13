"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DiscountRules(BaseSchema):
    # Order swagger.json

    
    value = fields.Int(required=False)
    
    type = fields.Str(required=False)
    

