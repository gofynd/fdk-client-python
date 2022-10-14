"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderDetailsData import OrderDetailsData

from .BagStatusHistory import BagStatusHistory





from .OrderBags import OrderBags



from .UserDetailsData import UserDetailsData

from .FulfillingStore import FulfillingStore







from .TrackingList import TrackingList

from .DPDetails import DPDetails

from .UserDetailsData import UserDetailsData



from .ShipmentPayments import ShipmentPayments

from .GST import GST









from .ShipmentStatusData import ShipmentStatusData





from .Prices import Prices


class Shipment(BaseSchema):
    # Orders swagger.json

    
    order = fields.Nested(OrderDetailsData, required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    packaging_type = fields.Str(required=False)
    
    platform_logo = fields.Str(required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    
    total_items = fields.Int(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    picked_date = fields.Str(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    user_agent = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    priority_text = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    shipment_id = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    

