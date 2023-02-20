"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ShipmentStatusData import ShipmentStatusData



from .OrderBags import OrderBags





from .BagStatusHistory import BagStatusHistory

















from .TrackingList import TrackingList





from .UserDetailsData import UserDetailsData



from .FulfillingStore import FulfillingStore







from .Prices import Prices



from .GSTDetailsData import GSTDetailsData







from .ShipmentPayments import ShipmentPayments







from .OrderDetailsData import OrderDetailsData



from .DPDetailsData import DPDetailsData







from .UserDetailsData import UserDetailsData





class PlatformShipment(BaseSchema):
    #  swagger.json

    
    vertical = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    platform_logo = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    
    enable_dp_tracking = fields.Boolean(required=False)
    
    priority_text = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    picked_date = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    user_agent = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    coupon = fields.Dict(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    total_bags = fields.Int(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    shipment_status = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    shipment_id = fields.Str(required=False)
    
