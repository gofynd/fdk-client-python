"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .BagStateMapper import BagStateMapper







class BagCurrentStatus(BaseSchema):
    #  swagger.json

    
    updated_at = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    status = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
