"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .OrderBags import OrderBags

from .OrderDetailsData import OrderDetailsData



from .OrderingStoreDetails import OrderingStoreDetails

from .ShipmentStatusData import ShipmentStatusData

from .AffiliateDetails import AffiliateDetails

from .DPDetailsData import DPDetailsData



from .InvoiceInfo import InvoiceInfo





from .Prices import Prices

from .UserDetailsData import UserDetailsData



from .FulfillingStore import FulfillingStore





from .GSTDetailsData import GSTDetailsData







from .BagStatusHistory import BagStatusHistory





from .TrackingList import TrackingList

from .Meta import Meta









from .ShipmentPayments import ShipmentPayments







from .UserDetailsData import UserDetailsData






class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    total_items = fields.Int(required=False)
    
    invoice_id = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    operational_status = fields.Str(required=False)
    
    ordering_store = fields.Nested(OrderingStoreDetails, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    priority_text = fields.Str(required=False)
    
    invoice = fields.Nested(InvoiceInfo, required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    enable_dp_tracking = fields.Boolean(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    fulfilment_priority = fields.Int(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    platform_logo = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    forward_shipment_id = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    vertical = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    coupon = fields.Dict(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    picked_date = fields.Str(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    user_agent = fields.Str(required=False)
    
    shipment_status = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    journey_type = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    

