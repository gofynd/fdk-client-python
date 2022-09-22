"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentData import ShipmentData

from .AffiliateBag import AffiliateBag







from .UserData import UserData



from .OrderUser import OrderUser

from .OrderUser import OrderUser











from .OrderPriority import OrderPriority


class OrderInfo(BaseSchema):
    # Order swagger.json

    
    shipment = fields.Nested(ShipmentData, required=False)
    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    discount = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    coupon = fields.Str(required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment = fields.Dict(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    order_value = fields.Float(required=False)
    
    items = fields.Dict(required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    

