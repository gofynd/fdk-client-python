"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PlatformChannel import PlatformChannel



from .PlatformShipment1 import PlatformShipment1







from .PlatformBreakupValues1 import PlatformBreakupValues1







from .UserDataInfo import UserDataInfo





class PlatformOrderItems(BaseSchema):
    #  swagger.json

    
    order_value = fields.Float(required=False)
    
    channel = fields.Nested(PlatformChannel, required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment1, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues1, required=False), required=False)
    
    total_order_value = fields.Float(required=False)
    
    order_id = fields.Str(required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    meta = fields.Dict(required=False)
    
