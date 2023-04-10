"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderBags import OrderBags

from .ShipmentStatusData import ShipmentStatusData

from .OrderDetailsData import OrderDetailsData









from .AffiliateDetails import AffiliateDetails





from .OrderingStoreDetails import OrderingStoreDetails

from .UserDataInfo import UserDataInfo

from .ShipmentPayments import ShipmentPayments







from .InvoiceInfo import InvoiceInfo



from .DPDetailsData import DPDetailsData







from .UserDetailsData import UserDetailsData



from .Meta import Meta

from .UserDetailsData import UserDetailsData



from .CompanyDetails import CompanyDetails











from .Prices import Prices

from .GSTDetailsData import GSTDetailsData





from .BagStatusHistory import BagStatusHistory

from .FulfillingStore import FulfillingStore

from .TrackingList import TrackingList






class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    journey_type = fields.Str(required=False)
    
    priority_text = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    fulfilment_priority = fields.Int(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    picked_date = fields.Str(required=False)
    
    coupon = fields.Dict(required=False)
    
    ordering_store = fields.Nested(OrderingStoreDetails, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    invoice_id = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    invoice = fields.Nested(InvoiceInfo, required=False)
    
    operational_status = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    total_bags = fields.Int(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    platform_logo = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    enable_dp_tracking = fields.Boolean(required=False)
    
    company_details = fields.Nested(CompanyDetails, required=False)
    
    payment_mode = fields.Str(required=False)
    
    shipment_status = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    vertical = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    forward_shipment_id = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    

