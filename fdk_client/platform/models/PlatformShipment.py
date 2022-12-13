"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserDetailsData import UserDetailsData









from .DPDetailsData import DPDetailsData



from .ShipmentPayments import ShipmentPayments



from .TrackingList import TrackingList



from .OrderDetailsData import OrderDetailsData





from .FulfillingStore import FulfillingStore









from .ShipmentStatusData import ShipmentStatusData





from .UserDetailsData import UserDetailsData

from .OrderBags import OrderBags





from .Prices import Prices



from .GSTDetailsData import GSTDetailsData

from .BagStatusHistory import BagStatusHistory


class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    operational_status = fields.Str(required=False)
    
    shipment_status = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    total_items = fields.Int(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    total_bags = fields.Int(required=False)
    
    packaging_type = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    picked_date = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    vertical = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    user_agent = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    

