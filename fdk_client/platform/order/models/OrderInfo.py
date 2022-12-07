"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .OrderUser import OrderUser







from .UserData import UserData



from .AffiliateBag import AffiliateBag





from .OrderUser import OrderUser









from .ShipmentData import ShipmentData







from .OrderPriority import OrderPriority





class OrderInfo(BaseSchema):
    #  swagger.json

    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    discount = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    cod_charges = fields.Float(required=False)
    
    items = fields.Dict(required=False)
    
    order_value = fields.Float(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    payment = fields.Dict(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    delivery_charges = fields.Float(required=False)
    
