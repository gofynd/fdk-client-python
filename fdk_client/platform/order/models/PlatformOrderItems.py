"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PlatformChannel import PlatformChannel



from .PlatformBreakupValues import PlatformBreakupValues





from .UserDataInfo import UserDataInfo







from .PlatformShipment import PlatformShipment









class PlatformOrderItems(BaseSchema):
    #  swagger.json

    
    channel = fields.Nested(PlatformChannel, required=False)
    
    breakup_values = fields.List(fields.Nested(PlatformBreakupValues, required=False), required=False)
    
    total_order_value = fields.Float(required=False)
    
    user_info = fields.Nested(UserDataInfo, required=False)
    
    payment_mode = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipment, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    order_created_time = fields.Str(required=False)
    
    order_value = fields.Float(required=False)
    
