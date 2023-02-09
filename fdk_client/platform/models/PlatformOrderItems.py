"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .UserDataInfo import UserDataInfo



from .PlatformBreakupValues import PlatformBreakupValues



from .PlatformChannel import PlatformChannel

from .PlatformShipment import PlatformShipment






class PlatformOrderItems(BaseSchema):
    # Orders swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    total_order_value = fields.Float(required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues, required=False), required=False)
    
    order_value = fields.Float(required=False)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    order_created_time = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

