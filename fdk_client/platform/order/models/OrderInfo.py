"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ShipmentData import ShipmentData







from .AffiliateBag import AffiliateBag









from .OrderUser import OrderUser





from .UserData import UserData





from .OrderUser import OrderUser



from .OrderPriority import OrderPriority



class OrderInfo(BaseSchema):
    #  swagger.json

    
    payment = fields.Dict(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    delivery_charges = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    items = fields.Dict(required=False)
    
    coupon = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    discount = fields.Float(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    order_value = fields.Float(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
