"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OrderPriority import OrderPriority

from .UserData import UserData











from .ShipmentData import ShipmentData

from .AffiliateBag import AffiliateBag

from .OrderUser import OrderUser





from .OrderUser import OrderUser




class OrderInfo(BaseSchema):
    # Order swagger.json

    
    delivery_charges = fields.Float(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    user = fields.Nested(UserData, required=False)
    
    items = fields.Dict(required=False)
    
    cod_charges = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    order_value = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    discount = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    payment = fields.Dict(required=False)
    

