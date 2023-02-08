"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PlatformShipment import PlatformShipment









from .UserDataInfo import UserDataInfo





from .PlatformBreakupValues import PlatformBreakupValues





from .PlatformChannel import PlatformChannel





class PlatformOrderItems(BaseSchema):
    #  swagger.json

    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    order_value = fields.Float(required=False)
    
    order_created_time = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    total_order_value = fields.Float(required=False)
    
