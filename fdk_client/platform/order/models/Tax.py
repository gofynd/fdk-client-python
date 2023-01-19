"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Tax(BaseSchema):
    #  swagger.json

    
    amount = fields.Dict(required=False)
    
    rate = fields.Float(required=False)
    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
