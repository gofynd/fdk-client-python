"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Prices import Prices













from .BagStatusHistory import BagStatusHistory





from .GSTDetailsData import GSTDetailsData







from .TrackingList import TrackingList





from .DPDetailsData import DPDetailsData



from .ShipmentStatusData import ShipmentStatusData







from .UserDetailsData import UserDetailsData



from .OrderDetailsData import OrderDetailsData



from .OrderBags import OrderBags



from .FulfillingStore import FulfillingStore













from .UserDetailsData import UserDetailsData



from .ShipmentPayments import ShipmentPayments







class PlatformShipment1(BaseSchema):
    #  swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    operational_status = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    picked_date = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    shipment_status = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    total_items = fields.Int(required=False)
    
    total_bags = fields.Int(required=False)
    
    journey_type = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    user_agent = fields.Str(required=False)
    
