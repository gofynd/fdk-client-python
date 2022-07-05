"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderDetails import OrderDetails









from .FulfillingStore import FulfillingStore



from .UserDetails import UserDetails

from .ShipmentPrices import ShipmentPrices

from .UserDetails import UserDetails



from .DPDetails import DPDetails




class Shipment(BaseSchema):
    # Orders swagger.json

    
    order = fields.Nested(OrderDetails, required=False)
    
    payment_mode = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Str(required=False), required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    shipment_id = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetails, required=False)
    
    shipment_prices = fields.Nested(ShipmentPrices, required=False)
    
    billing_details = fields.Nested(UserDetails, required=False)
    
    journey_type = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    bags = fields.Dict(required=False)
    

