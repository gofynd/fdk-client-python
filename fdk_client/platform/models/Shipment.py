"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserDetailsData import UserDetailsData



from .ShipmentPayments import ShipmentPayments

from .TrackingList import TrackingList

from .OrderBags import OrderBags





from .ShipmentStatusData import ShipmentStatusData

from .DPDetails import DPDetails









from .GST import GST

from .UserDetailsData import UserDetailsData

from .Prices import Prices

from .OrderDetailsData import OrderDetailsData



from .FulfillingStore import FulfillingStore









from .BagStatusHistory import BagStatusHistory




class Shipment(BaseSchema):
    # Orders swagger.json

    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    platform_logo = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    priority_text = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    packaging_type = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    
    picked_date = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    

