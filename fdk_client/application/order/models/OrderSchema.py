"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Shipments import Shipments





from .UserInfo import UserInfo



from .BreakupValues import BreakupValues







from .BagsForReorder import BagsForReorder



class OrderSchema(BaseSchema):
    #  swagger.json

    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    order_created_time = fields.Str(required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
