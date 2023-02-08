"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Trader(BaseSchema):
    #  swagger.json

    
    address = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Raw(required=False)
    
    type = fields.Str(required=False)
    
