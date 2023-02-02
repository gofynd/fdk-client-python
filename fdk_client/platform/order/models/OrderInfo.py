"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateBag import AffiliateBag



from .ShipmentData import ShipmentData













from .OrderUser import OrderUser









from .OrderUser import OrderUser



from .OrderPriority import OrderPriority





from .UserData import UserData



class OrderInfo(BaseSchema):
    #  swagger.json

    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    payment_mode = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    items = fields.Dict(required=False)
    
    payment = fields.Dict(required=False)
    
    order_value = fields.Float(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    discount = fields.Float(required=False)
    
    user = fields.Nested(UserData, required=False)
    
