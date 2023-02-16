"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ShipmentPayments import ShipmentPayments



from .TrackingList import TrackingList







from .GSTDetailsData import GSTDetailsData





from .Prices import Prices











from .UserDetailsData import UserDetailsData



from .OrderDetailsData import OrderDetailsData



from .UserDetailsData import UserDetailsData















from .FulfillingStore import FulfillingStore





from .ShipmentStatusData import ShipmentStatusData



from .DPDetailsData import DPDetailsData





from .OrderBags import OrderBags



from .BagStatusHistory import BagStatusHistory









class PlatformShipment(BaseSchema):
    #  swagger.json

    
    shipment_id = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    user_agent = fields.Str(required=False)
    
    shipment_status = fields.Str(required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    operational_status = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    platform_logo = fields.Str(required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    total_items = fields.Int(required=False)
    
    packaging_type = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    coupon = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    picked_date = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    vertical = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    enable_dp_tracking = fields.Boolean(required=False)
    
    priority_text = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
