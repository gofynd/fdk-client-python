"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .FulfillingStore import FulfillingStore

from .ShipmentStatusData import ShipmentStatusData



from .TrackingList import TrackingList

from .UserDetailsData import UserDetailsData

from .Prices import Prices

from .DPDetails import DPDetails



from .GST import GST

from .UserDetailsData import UserDetailsData











from .OrderDetailsData import OrderDetailsData



from .ShipmentPayments import ShipmentPayments

from .OrderBags import OrderBags



from .BagStatusHistory import BagStatusHistory




class Shipment(BaseSchema):
    # Orders swagger.json

    
    enable_dp_tracking = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    user_agent = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    payment_mode = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    shipment_id = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    picked_date = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    total_items = fields.Int(required=False)
    
    vertical = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    packaging_type = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    platform_logo = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    journey_type = fields.Str(required=False)
    

