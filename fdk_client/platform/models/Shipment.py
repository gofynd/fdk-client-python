"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OrderDetailsData import OrderDetailsData



from .DPDetails import DPDetails

from .TrackingList import TrackingList









from .BagStatusHistory import BagStatusHistory

from .Prices import Prices

from .FulfillingStore import FulfillingStore

from .UserDetailsData import UserDetailsData



from .ShipmentPayments import ShipmentPayments









from .UserDetailsData import UserDetailsData

from .GST import GST





from .ShipmentStatusData import ShipmentStatusData

from .OrderBags import OrderBags


class Shipment(BaseSchema):
    # Orders swagger.json

    
    journey_type = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    user_agent = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    total_items = fields.Int(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    picked_date = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    priority_text = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    packaging_type = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    

