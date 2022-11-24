"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .OrderUser import OrderUser

from .ShipmentData import ShipmentData



from .OrderUser import OrderUser











from .AffiliateBag import AffiliateBag

from .UserData import UserData



from .OrderPriority import OrderPriority


class OrderInfo(BaseSchema):
    # Order swagger.json

    
    order_value = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    coupon = fields.Str(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment = fields.Dict(required=False)
    
    items = fields.Dict(required=False)
    
    cod_charges = fields.Float(required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    user = fields.Nested(UserData, required=False)
    
    delivery_charges = fields.Float(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    

