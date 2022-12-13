"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PlatformShipment1 import PlatformShipment1





from .PlatformChannel import PlatformChannel





from .UserDataInfo import UserDataInfo





from .PlatformBreakupValues1 import PlatformBreakupValues1









class PlatformOrderItems(BaseSchema):
    #  swagger.json

    
    shipments = fields.List(fields.Nested(PlatformShipment1, required=False), required=False)
    
    total_order_value = fields.Float(required=False)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    payment_mode = fields.Str(required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    order_value = fields.Float(required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues1, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
