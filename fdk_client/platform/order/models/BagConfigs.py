"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class BagConfigs(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    is_returnable = fields.Boolean(required=False)
    
    allow_force_return = fields.Boolean(required=False)
    
