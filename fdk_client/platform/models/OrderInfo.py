"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateBag import AffiliateBag



from .UserData import UserData

from .OrderPriority import OrderPriority







from .ShipmentData import ShipmentData







from .OrderUser import OrderUser

from .OrderUser import OrderUser






class OrderInfo(BaseSchema):
    # OrderManage swagger.json

    
    bags = fields.List(fields.Nested(AffiliateBag, required=False), required=False)
    
    payment = fields.Dict(required=False)
    
    user = fields.Nested(UserData, required=False)
    
    order_priority = fields.Nested(OrderPriority, required=False)
    
    cod_charges = fields.Float(required=False)
    
    items = fields.Dict(required=False)
    
    coupon = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentData, required=False)
    
    order_value = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    billing_address = fields.Nested(OrderUser, required=False)
    
    shipping_address = fields.Nested(OrderUser, required=False)
    
    payment_mode = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
