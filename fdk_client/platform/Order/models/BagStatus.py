"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .BagStatusBagStateMapper import BagStatusBagStateMapper



class BagStatus(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStatusBagStateMapper, required=False)
    
