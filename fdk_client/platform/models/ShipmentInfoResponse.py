"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .OrderDetailsData import OrderDetailsData









from .DPDetails import DPDetails

from .TrackingList import TrackingList



























from .BagStatusHistory import BagStatusHistory

from .Prices import Prices

























from .FulfillingStore import FulfillingStore

from .UserDetailsData import UserDetailsData





from .ShipmentPayments import ShipmentPayments









































from .UserDetailsData import UserDetailsData







from .GST import GST





from .ShipmentStatusData import ShipmentStatusData

from .OrderBags import OrderBags


class ShipmentInfoResponse(BaseSchema):
    # Orders swagger.json

    
    go_green = fields.Boolean(required=False)
    
    journey_type = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    user_agent = fields.Str(required=False)
    
    invoice = fields.Dict(required=False)
    
    user_info = fields.Dict(required=False)
    
    refund_text = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    total_items = fields.Int(required=False)
    
    kirana_store_id = fields.Str(required=False)
    
    is_fynd_store = fields.Str(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    order_created_time = fields.Str(required=False)
    
    forward_tracking_list = fields.List(fields.Dict(required=False), required=False)
    
    bank_data = fields.Dict(required=False)
    
    mid = fields.Str(required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    email_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    pay_button = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    is_invoiced = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    is_packaging_order = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    refund_details = fields.Dict(required=False)
    
    is_fynd_coupon = fields.Boolean(required=False)
    
    coupon = fields.Dict(required=False)
    
    replacement_details = fields.Str(required=False)
    
    is_not_fynd_source = fields.Boolean(required=False)
    
    order_type = fields.Str(required=False)
    
    status_progress = fields.Int(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    picked_date = fields.Str(required=False)
    
    order_status = fields.Dict(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    priority_text = fields.Str(required=False)
    
    delivery_status = fields.List(fields.Dict(required=False), required=False)
    
    is_pdsr = fields.Str(required=False)
    
    child_nodes = fields.List(fields.Str(required=False), required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    ordering_store = fields.Dict(required=False)
    
    platform_logo = fields.Boolean(required=False)
    
    current_shipment_status = fields.Dict(required=False)
    
    secured_delivery_flag = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    company = fields.Dict(required=False)
    
    due_date = fields.Str(required=False)
    
    forward_shipment_status = fields.List(fields.Dict(required=False), required=False)
    
    credit_note_id = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    payment_mode = fields.Str(required=False)
    
    escalation = fields.Dict(required=False)
    
    tracking_url = fields.Str(required=False)
    
    can_break = fields.Str(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    lock_status = fields.Str(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    forward_order_status = fields.List(fields.Dict(required=False), required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    packaging_type = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    bags = fields.Nested(OrderBags, required=False)
    

