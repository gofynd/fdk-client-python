"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .OrderPriority import OrderPriority



from .AffiliateBag import AffiliateBag





from .OrderUser import OrderUser



from .OrderUser import OrderUser



from .UserData import UserData









from .ShipmentData import ShipmentData





class OrderInfo(BaseSchema):
    #  swagger.json

    
    delivery_charges = fields.Float(required=False)
    
    payment = fields.Dict(required=False)
    
    order_value = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    cod_charges = fields.Float(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    user = fields.Nested(UserData, required=False)
    
    items = fields.Dict(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    coupon = fields.Str(required=False)
    
