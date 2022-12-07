"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateBag import AffiliateBag









from .OrderUser import OrderUser





from .ShipmentData import ShipmentData



from .UserData import UserData





from .OrderUser import OrderUser









from .OrderPriority import OrderPriority





class OrderInfo(BaseSchema):
    #  swagger.json

    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    delivery_charges = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    user = fields.Nested(UserData, required=False)
    
    items = fields.Dict(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    payment = fields.Dict(required=False)
    
    order_value = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    coupon = fields.Str(required=False)
    
