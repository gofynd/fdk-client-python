"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Tax import Tax








class Charge(BaseSchema):
    # Order swagger.json

    
    amount = fields.Dict(required=False)
    
    tax = fields.Nested(Tax, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

