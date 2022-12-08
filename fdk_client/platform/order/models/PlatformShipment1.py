"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ShipmentPayments import ShipmentPayments





from .UserDetailsData import UserDetailsData



from .TrackingList import TrackingList



from .BagStatusHistory import BagStatusHistory









from .GSTDetailsData import GSTDetailsData











from .UserDetailsData import UserDetailsData



from .FulfillingStore import FulfillingStore



from .OrderDetailsData import OrderDetailsData



from .Prices import Prices









from .DPDetailsData import DPDetailsData











from .OrderBags import OrderBags







from .ShipmentStatusData import ShipmentStatusData



class PlatformShipment1(BaseSchema):
    #  swagger.json

    
    picked_date = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    total_items = fields.Int(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    user_agent = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    platform_logo = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    total_bags = fields.Int(required=False)
    
    packaging_type = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    payment_mode = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    journey_type = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    shipment_status = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
