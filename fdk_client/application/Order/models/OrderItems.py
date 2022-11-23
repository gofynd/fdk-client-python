"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .UserInfo import UserInfo





from .ShipmentResponse import ShipmentResponse





from .PricesBreakup import PricesBreakup





from .BagsForReorder import BagsForReorder



class OrderItems(BaseSchema):
    #  swagger.json

    
    user_info = fields.Nested(UserInfo, required=False)
    
    order_created_time = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(PricesBreakup, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
