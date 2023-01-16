"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Tax import Tax









class Charge(BaseSchema):
    #  swagger.json

    
    amount = fields.Dict(required=False)
    
    tax = fields.Nested(Tax, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    