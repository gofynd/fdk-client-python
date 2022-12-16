"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SubLane import SubLane









class SuperLane(BaseSchema):
    #  swagger.json

    
    options = fields.List(fields.Nested(SubLane, required=False), required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    
