"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .BagStatusHistory import BagStatusHistory







from .FulfillingStore import FulfillingStore





from .OrderBags import OrderBags







from .Prices import Prices



from .OrderDetailsData import OrderDetailsData







from .UserDetailsData import UserDetailsData



from .GSTDetailsData import GSTDetailsData





from .DPDetailsData import DPDetailsData



from .TrackingList import TrackingList





from .UserDetailsData import UserDetailsData







from .ShipmentStatusData import ShipmentStatusData







from .ShipmentPayments import ShipmentPayments



class PlatformShipment1(BaseSchema):
    #  swagger.json

    
    total_items = fields.Int(required=False)
    
    priority_text = fields.Str(required=False)
    
    picked_date = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    shipment_status = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    operational_status = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    user_agent = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    journey_type = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    packaging_type = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    vertical = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
