"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PlatformShipment import PlatformShipment







from .PlatformChannel import PlatformChannel

from .PlatformBreakupValues import PlatformBreakupValues



from .UserDataInfo import UserDataInfo


class PlatformOrderItems(BaseSchema):
    # Order swagger.json

    
    order_value = fields.Float(required=False)
    
    order_created_time = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    total_order_value = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    

