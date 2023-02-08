"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OrderUser import OrderUser



from .ShipmentData import ShipmentData



from .OrderUser import OrderUser









from .OrderPriority import OrderPriority





from .UserData import UserData







from .AffiliateBag import AffiliateBag







class OrderInfo(BaseSchema):
    #  swagger.json

    
    payment = fields.Dict(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    discount = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    order_value = fields.Float(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    coupon = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    delivery_charges = fields.Float(required=False)
    
    items = fields.Dict(required=False)
    
