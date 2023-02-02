"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Tax(BaseSchema):
    #  swagger.json

    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    amount = fields.Dict(required=False)
    
