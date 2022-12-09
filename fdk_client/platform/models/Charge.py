"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Tax import Tax




class Charge(BaseSchema):
    # OrderManage swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    tax = fields.Nested(Tax, required=False)
    
    amount = fields.Dict(required=False)
    

