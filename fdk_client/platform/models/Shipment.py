"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .FulfillingStore import FulfillingStore



from .GST import GST













from .ShipmentPayments import ShipmentPayments





from .UserDetailsData import UserDetailsData

from .ShipmentStatusData import ShipmentStatusData

from .UserDetailsData import UserDetailsData



from .TrackingList import TrackingList



from .DPDetails import DPDetails



from .Prices import Prices

from .OrderBags import OrderBags

from .BagStatusHistory import BagStatusHistory

from .OrderDetailsData import OrderDetailsData


class Shipment(BaseSchema):
    # Order swagger.json

    
    priority_text = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    picked_date = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    vertical = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    total_items = fields.Int(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    payment_mode = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    

