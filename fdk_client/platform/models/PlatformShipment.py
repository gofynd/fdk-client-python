"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UserDetailsData import UserDetailsData



from .TrackingList import TrackingList

from .FulfillingStore import FulfillingStore



from .OrderBags import OrderBags

from .DPDetailsData import DPDetailsData

from .GSTDetailsData import GSTDetailsData







from .UserDetailsData import UserDetailsData





from .Prices import Prices



from .BagStatusHistory import BagStatusHistory







from .ShipmentStatusData import ShipmentStatusData



from .ShipmentPayments import ShipmentPayments









from .OrderDetailsData import OrderDetailsData




class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    shipment_status = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    priority_text = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    picked_date = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    total_items = fields.Int(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    platform_logo = fields.Str(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    user_agent = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    shipment_id = fields.Str(required=False)
    

