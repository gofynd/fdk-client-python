"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DPDetails import DPDetails





from .UserDetailsData import UserDetailsData



from .ShipmentGSTData import ShipmentGSTData

from .TrackingList import TrackingList









from .ShipmentPayments import ShipmentPayments

from .BagStatusHistory import BagStatusHistory



from .OrderDetailsData import OrderDetailsData

from .ShipmentStatusData import ShipmentStatusData

from .UserDetailsData import UserDetailsData







from .FulfillingStore import FulfillingStore








class Shipment(BaseSchema):
    # Orders swagger.json

    
    dp_details = fields.Nested(DPDetails, required=False)
    
    platform_logo = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    journey_type = fields.Str(required=False)
    
    gst_details = fields.Nested(ShipmentGSTData, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    picked_date = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    bags = fields.Dict(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    vertical = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    payment_mode = fields.Str(required=False)
    
    prices = fields.Dict(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    user_agent = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    priority_text = fields.Str(required=False)
    

