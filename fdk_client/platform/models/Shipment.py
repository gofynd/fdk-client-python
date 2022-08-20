"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .UserDetailsData import UserDetailsData



from .FulfillingStore import FulfillingStore



from .GST import GST

from .UserDetailsData import UserDetailsData

from .TrackingList import TrackingList

from .OrderDetailsData import OrderDetailsData



from .OrderBags import OrderBags

from .ShipmentStatusData import ShipmentStatusData

from .DPDetails import DPDetails

from .ShipmentPayments import ShipmentPayments







from .Prices import Prices



from .BagStatusHistory import BagStatusHistory




class Shipment(BaseSchema):
    # Orders swagger.json

    
    picked_date = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    total_items = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    packaging_type = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    platform_logo = fields.Str(required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    vertical = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    journey_type = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    

