"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Trader(BaseSchema):
    #  swagger.json

    
    name = fields.Raw(required=False)
    
    address = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
