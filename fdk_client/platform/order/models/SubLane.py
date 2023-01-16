"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class SubLane(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    actions = fields.List(fields.Dict(required=False), required=False)
    
    index = fields.Int(required=False)
    
    total_items = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
