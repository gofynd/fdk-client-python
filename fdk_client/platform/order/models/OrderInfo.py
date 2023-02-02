"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .AffiliateBag import AffiliateBag







from .UserData import UserData



from .OrderUser import OrderUser



from .OrderUser import OrderUser



from .ShipmentData import ShipmentData











from .OrderPriority import OrderPriority





class OrderInfo(BaseSchema):
    #  swagger.json

    
    items = fields.Dict(required=False)
    
    coupon = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    order_value = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    payment_mode = fields.Str(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    payment = fields.Dict(required=False)
    
