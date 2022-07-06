"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderDetailsData import OrderDetailsData

from .FulfillingStore import FulfillingStore







from .DPDetails import DPDetails



from .UserDetailsData import UserDetailsData

from .ShipmentPricesData import ShipmentPricesData







from .UserDetailsData import UserDetailsData


class Shipment(BaseSchema):
    # Orders swagger.json

    
    order = fields.Nested(OrderDetailsData, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    bags = fields.Dict(required=False)
    
    journey_type = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    shipment_prices = fields.Nested(ShipmentPricesData, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    bag_status_history = fields.List(fields.Str(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    

