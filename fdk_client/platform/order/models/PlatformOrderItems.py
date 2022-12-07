"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .PlatformChannel import PlatformChannel





from .UserDataInfo import UserDataInfo



from .PlatformBreakupValues1 import PlatformBreakupValues1







from .PlatformShipment1 import PlatformShipment1





class PlatformOrderItems(BaseSchema):
    #  swagger.json

    
    payment_mode = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    total_order_value = fields.Float(required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues1, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment1, required=False), required=False)
    
    order_value = fields.Float(required=False)
    
