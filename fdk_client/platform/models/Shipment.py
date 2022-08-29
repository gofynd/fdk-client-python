"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .DPDetails import DPDetails

from .ShipmentStatusData import ShipmentStatusData



from .TrackingList import TrackingList

from .GST import GST

from .Prices import Prices





from .UserDetailsData import UserDetailsData





from .OrderDetailsData import OrderDetailsData



from .FulfillingStore import FulfillingStore





from .ShipmentPayments import ShipmentPayments

from .UserDetailsData import UserDetailsData



from .BagStatusHistory import BagStatusHistory

from .OrderBags import OrderBags






class Shipment(BaseSchema):
    # Orders swagger.json

    
    priority_text = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    packaging_type = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    picked_date = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    journey_type = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    shipment_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    platform_logo = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    vertical = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    

