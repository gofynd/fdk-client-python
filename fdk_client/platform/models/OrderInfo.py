"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderUser import OrderUser



from .ShipmentData import ShipmentData



from .OrderPriority import OrderPriority





from .UserData import UserData











from .AffiliateBag import AffiliateBag

from .OrderUser import OrderUser


class OrderInfo(BaseSchema):
    # Order swagger.json

    
    billing_address = fields.Nested(OrderUser, required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    payment = fields.Dict(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    items = fields.Dict(required=False)
    
    discount = fields.Float(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    order_value = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    coupon = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    

