"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .UserDetailsData import UserDetailsData







from .BagStatusHistory import BagStatusHistory























from .OrderDetailsData import OrderDetailsData



































from .GSTDetailsData import GSTDetailsData

















from .TrackingList import TrackingList



















from .UserDetailsData import UserDetailsData

















from .ShipmentPayments import ShipmentPayments









from .DPDetailsData import DPDetailsData







from .OrderBags import OrderBags









from .FulfillingStore import FulfillingStore





from .ShipmentStatusData import ShipmentStatusData





from .Prices import Prices







class ShipmentInfoResponse(BaseSchema):
    #  swagger.json

    
    can_cancel = fields.Boolean(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    
    is_fynd_coupon = fields.Boolean(required=False)
    
    secured_delivery_flag = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    is_invoiced = fields.Boolean(required=False)
    
    shipment_status = fields.Str(required=False)
    
    invoice = fields.Dict(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    total_bags = fields.Int(required=False)
    
    is_not_fynd_source = fields.Boolean(required=False)
    
    order_status = fields.Dict(required=False)
    
    due_date = fields.Str(required=False)
    
    kirana_store_id = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    is_packaging_order = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    delivery_status = fields.List(fields.Dict(required=False), required=False)
    
    total_items = fields.Int(required=False)
    
    status_progress = fields.Int(required=False)
    
    ordering_store = fields.Dict(required=False)
    
    mid = fields.Str(required=False)
    
    refund_text = fields.Str(required=False)
    
    coupon = fields.Dict(required=False)
    
    tracking_url = fields.Str(required=False)
    
    current_shipment_status = fields.Dict(required=False)
    
    is_fynd_store = fields.Str(required=False)
    
    user_info = fields.Dict(required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    gst_details = fields.Nested(GSTDetailsData, required=False)
    
    can_return = fields.Boolean(required=False)
    
    refund_details = fields.Dict(required=False)
    
    is_pdsr = fields.Str(required=False)
    
    forward_tracking_list = fields.List(fields.Dict(required=False), required=False)
    
    forward_order_status = fields.List(fields.Dict(required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    operational_status = fields.Str(required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    go_green = fields.Boolean(required=False)
    
    replacement_details = fields.Str(required=False)
    
    child_nodes = fields.List(fields.Str(required=False), required=False)
    
    picked_date = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    user_agent = fields.Str(required=False)
    
    can_break = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    lock_status = fields.Str(required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    forward_shipment_status = fields.List(fields.Dict(required=False), required=False)
    
    escalation = fields.Dict(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    order_created_time = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    pay_button = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetailsData, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    bank_data = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(OrderBags, required=False), required=False)
    
    email_id = fields.Str(required=False)
    
    platform_logo = fields.Boolean(required=False)
    
    order_type = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    priority_text = fields.Str(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    credit_note_id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    company = fields.Dict(required=False)
    
    vertical = fields.Str(required=False)
    
