"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserDetailsData import UserDetailsData



from .FulfillingStore import FulfillingStore

from .ShipmentPricesData import ShipmentPricesData

from .DPDetails import DPDetails









from .OrderDetailsData import OrderDetailsData



from .UserDetailsData import UserDetailsData




class Shipment(BaseSchema):
    # Orders swagger.json

    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    bag_status_history = fields.List(fields.Str(required=False), required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    shipment_prices = fields.Nested(ShipmentPricesData, required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    journey_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    bags = fields.Dict(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    payment_mode = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    shipment_quantity = fields.Int(required=False)
    

