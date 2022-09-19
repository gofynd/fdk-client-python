"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices



from .UserDetailsData import UserDetailsData



from .BagStatusHistory import BagStatusHistory









from .ShipmentStatusData import ShipmentStatusData

from .OrderDetailsData import OrderDetailsData



from .ShipmentPayments import ShipmentPayments





from .OrderBags import OrderBags



from .TrackingList import TrackingList



from .UserDetailsData import UserDetailsData

from .DPDetails import DPDetails

from .GST import GST





from .FulfillingStore import FulfillingStore


class Shipment(BaseSchema):
    # Orders swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    priority_text = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    platform_logo = fields.Str(required=False)
    
    picked_date = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    vertical = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    journey_type = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    payment_mode = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    packaging_type = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    

