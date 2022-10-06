"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .TrackingList import TrackingList

from .BagStatusHistory import BagStatusHistory

from .DPDetails import DPDetails



from .OrderBags import OrderBags

from .FulfillingStore import FulfillingStore

from .UserDetailsData import UserDetailsData







from .UserDetailsData import UserDetailsData

from .OrderDetailsData import OrderDetailsData

from .ShipmentStatusData import ShipmentStatusData

from .ShipmentPayments import ShipmentPayments





from .GST import GST













from .Prices import Prices


class Shipment(BaseSchema):
    # Orders swagger.json

    
    shipment_id = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    total_items = fields.Int(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    vertical = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    platform_logo = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    journey_type = fields.Str(required=False)
    
    picked_date = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    

