"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .ShipmentData import ShipmentData





from .OrderUser import OrderUser







from .OrderPriority import OrderPriority





from .AffiliateBag import AffiliateBag





from .OrderUser import OrderUser



from .UserData import UserData





class OrderInfo(BaseSchema):
    #  swagger.json

    
    affiliate_order_id = fields.Str(required=False)
    
    payment = fields.Dict(required=False)
    
    order_value = fields.Float(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    discount = fields.Float(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    cod_charges = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    items = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    delivery_charges = fields.Float(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    user = fields.Nested(UserData, required=False)
    
    payment_mode = fields.Str(required=False)
    
