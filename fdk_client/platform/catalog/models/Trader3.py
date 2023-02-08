"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Trader3(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    address = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
