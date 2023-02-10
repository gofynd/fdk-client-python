"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentData import ShipmentData









from .UserData import UserData







from .OrderPriority import OrderPriority



from .AffiliateBag import AffiliateBag



from .OrderUser import OrderUser







from .OrderUser import OrderUser







class OrderInfo(BaseSchema):
    #  swagger.json

    
    shipment = fields.Nested(ShipmentData, required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    order_value = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    payment = fields.Dict(required=False)
    
    cod_charges = fields.Float(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    coupon = fields.Str(required=False)
    
    items = fields.Dict(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    discount = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
