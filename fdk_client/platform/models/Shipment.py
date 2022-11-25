"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .DPDetails import DPDetails

from .UserDetailsData import UserDetailsData

from .TrackingList import TrackingList



from .UserDetailsData import UserDetailsData







from .GST import GST



from .BagStatusHistory import BagStatusHistory

from .ShipmentStatusData import ShipmentStatusData







from .OrderDetailsData import OrderDetailsData

from .ShipmentPayments import ShipmentPayments







from .Prices import Prices

from .FulfillingStore import FulfillingStore

from .OrderBags import OrderBags


class Shipment(BaseSchema):
    # Order swagger.json

    
    picked_date = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    user_agent = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    vertical = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    packaging_type = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    priority_text = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    total_items = fields.Int(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    journey_type = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    

