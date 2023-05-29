"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class FinancialBreakup(BaseSchema):
    pass


class OrderBagItem(BaseSchema):
    pass


class BagConfigs(BaseSchema):
    pass


class BagGST(BaseSchema):
    pass


class OrderBrandName(BaseSchema):
    pass


class OrderBagArticle(BaseSchema):
    pass


class OrderBags(BaseSchema):
    pass


class GST(BaseSchema):
    pass


class DPDetails(BaseSchema):
    pass


class ShipmentStatusData(BaseSchema):
    pass


class OrderDetailsData(BaseSchema):
    pass


class ShipmentPayments(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class UserDetailsData(BaseSchema):
    pass


class BagStatusHistory(BaseSchema):
    pass


class TrackingList(BaseSchema):
    pass


class ShipmentInfoResponse(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class SubLane(BaseSchema):
    pass


class SuperLane(BaseSchema):
    pass


class LaneConfigResponse(BaseSchema):
    pass


class OrderDict(BaseSchema):
    pass


class Shipment(BaseSchema):
    pass


class ShipmentDetailsResponse(BaseSchema):
    pass


class FilterInfoOption(BaseSchema):
    pass


class FiltersInfo(BaseSchema):
    pass


class PaymentModeInfo(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class BagUnit(BaseSchema):
    pass


class ShipmentStatus(BaseSchema):
    pass


class UserDataInfo(BaseSchema):
    pass


class ShipmentItemFulFillingStore(BaseSchema):
    pass


class ShipmentItem(BaseSchema):
    pass


class ShipmentInternalPlatformViewResponse(BaseSchema):
    pass


class ShipmentPricesDataSet(BaseSchema):
    pass


class Shipment1(BaseSchema):
    pass


class ManifestShipmentResponse(BaseSchema):
    pass


class ErrorSchemaDataSet(BaseSchema):
    pass


class ShipmentPricesDataInfo(BaseSchema):
    pass


class ShipmentDataSet(BaseSchema):
    pass


class UserDataSet(BaseSchema):
    pass


class OrderDataSet(BaseSchema):
    pass


class OrderListingResponse(BaseSchema):
    pass


class OrderErrorSchemaDataSet(BaseSchema):
    pass


class Options(BaseSchema):
    pass


class MetricsCount(BaseSchema):
    pass


class MetricCountResponse(BaseSchema):
    pass


class FiltersResponse(BaseSchema):
    pass


class Success(BaseSchema):
    pass


class OmsReports(BaseSchema):
    pass


class JioCodeUpsertDataSet(BaseSchema):
    pass


class JioCodeUpsertPayload(BaseSchema):
    pass


class NestedErrorSchemaDataSet(BaseSchema):
    pass


class JioCodeUpsertResponse(BaseSchema):
    pass


class ProductDetail(BaseSchema):
    pass


class ShipmentBody(BaseSchema):
    pass


class ShipmentDetail(BaseSchema):
    pass


class Statuses(BaseSchema):
    pass


class PlatformShipmentStatusInternal(BaseSchema):
    pass


class ResponseDetail(BaseSchema):
    pass


class ErrorDetail(BaseSchema):
    pass


class HistoryDict(BaseSchema):
    pass


class ShipmentHistoryResponse(BaseSchema):
    pass


class PlatformOrderUpdate(BaseSchema):
    pass





class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    amount_paid = fields.Int(required=False)
    
    discount = fields.Int(required=False)
    
    value_of_good = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    identifiers = fields.Dict(required=False)
    
    transfer_price = fields.Int(required=False)
    
    cashback = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    gst_fee = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    coupon_effective_discount = fields.Int(required=False)
    
    refund_credit = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    coupon_value = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    promotion_effective_discount = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    total_units = fields.Int(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    price_marked = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    pm_price_split = fields.Dict(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    


class OrderBagItem(BaseSchema):
    # Order swagger.json

    
    image = fields.List(fields.Str(required=False), required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    l3_category = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    


class BagConfigs(BaseSchema):
    # Order swagger.json

    
    is_returnable = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    
    allow_force_return = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    


class BagGST(BaseSchema):
    # Order swagger.json

    
    hsn_code = fields.Str(required=False)
    
    value_of_good = fields.Int(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_fee = fields.Int(required=False)
    
    gst_tag = fields.Str(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    


class OrderBrandName(BaseSchema):
    # Order swagger.json

    
    created_on = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    
    modified_on = fields.Int(required=False)
    
    company = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class OrderBagArticle(BaseSchema):
    # Order swagger.json

    
    return_config = fields.Dict(required=False)
    
    identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    


class OrderBags(BaseSchema):
    # Order swagger.json

    
    entity_type = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    item = fields.Nested(OrderBagItem, required=False)
    
    current_status = fields.Str(required=False)
    
    bag_configs = fields.Nested(BagConfigs, required=False)
    
    display_name = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGST, required=False)
    
    bag_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    brand = fields.Nested(OrderBrandName, required=False)
    
    article = fields.Nested(OrderBagArticle, required=False)
    


class GST(BaseSchema):
    # Order swagger.json

    
    value_of_good = fields.Float(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_fee = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    


class DPDetails(BaseSchema):
    # Order swagger.json

    
    eway_bill_id = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    track_url = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class ShipmentStatusData(BaseSchema):
    # Order swagger.json

    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class OrderDetailsData(BaseSchema):
    # Order swagger.json

    
    order_value = fields.Str(required=False)
    
    ordering_channel_logo = fields.Dict(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    cod_charges = fields.Str(required=False)
    
    tax_details = fields.Dict(required=False)
    
    source = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    order_date = fields.Str(required=False)
    


class ShipmentPayments(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    value_of_good = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    fulfillment_channel = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    phone = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class UserDetailsData(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class BagStatusHistory(BaseSchema):
    # Order swagger.json

    
    display_name = fields.Boolean(required=False)
    
    app_display_name = fields.Boolean(required=False)
    
    updated_at = fields.Str(required=False)
    
    forward = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    state_type = fields.Boolean(required=False)
    


class TrackingList(BaseSchema):
    # Order swagger.json

    
    is_current = fields.Boolean(required=False)
    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    


class ShipmentInfoResponse(BaseSchema):
    # Order swagger.json

    
    bags = fields.Nested(OrderBags, required=False)
    
    forward_shipment_status = fields.List(fields.Dict(required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    forward_tracking_list = fields.List(fields.Dict(required=False), required=False)
    
    refund_text = fields.Str(required=False)
    
    is_fynd_store = fields.Str(required=False)
    
    company = fields.Dict(required=False)
    
    user_id = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    payment_mode = fields.Str(required=False)
    
    refund_details = fields.Dict(required=False)
    
    user_info = fields.Dict(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    order_status = fields.Dict(required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    is_pdsr = fields.Str(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    can_break = fields.Str(required=False)
    
    go_green = fields.Boolean(required=False)
    
    delivery_status = fields.List(fields.Dict(required=False), required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    bank_data = fields.Dict(required=False)
    
    coupon = fields.Dict(required=False)
    
    lock_status = fields.Str(required=False)
    
    vertical = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    ordering_store = fields.Dict(required=False)
    
    total_items = fields.Int(required=False)
    
    child_nodes = fields.List(fields.Str(required=False), required=False)
    
    priority_text = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
    replacement_details = fields.Str(required=False)
    
    tracking_url = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    pay_button = fields.Str(required=False)
    
    email_id = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    due_date = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    mid = fields.Str(required=False)
    
    kirana_store_id = fields.Str(required=False)
    
    status_progress = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False)
    
    current_shipment_status = fields.Dict(required=False)
    
    escalation = fields.Dict(required=False)
    
    secured_delivery_flag = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    forward_order_status = fields.List(fields.Dict(required=False), required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    picked_date = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    is_packaging_order = fields.Boolean(required=False)
    
    platform_logo = fields.Boolean(required=False)
    
    invoice = fields.Dict(required=False)
    
    is_invoiced = fields.Boolean(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    is_fynd_coupon = fields.Boolean(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    enable_tracking = fields.Boolean(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    is_not_fynd_source = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    


class Error(BaseSchema):
    # Order swagger.json

    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class SubLane(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    current_state = fields.List(fields.Str(required=False), required=False)
    
    value = fields.Str(required=False)
    
    total_shipments = fields.Int(required=False)
    
    next_state = fields.List(fields.Str(required=False), required=False)
    
    index = fields.Int(required=False)
    


class SuperLane(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(SubLane, required=False), required=False)
    


class LaneConfigResponse(BaseSchema):
    # Order swagger.json

    
    super_lanes = fields.List(fields.Nested(SuperLane, required=False), required=False)
    


class OrderDict(BaseSchema):
    # Order swagger.json

    
    shipment_count = fields.Int(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    is_validated = fields.Boolean(required=False)
    
    order_date = fields.Str(required=False)
    


class Shipment(BaseSchema):
    # Order swagger.json

    
    bags = fields.Nested(OrderBags, required=False)
    
    journey_type = fields.Str(required=False)
    
    gst_details = fields.Nested(GST, required=False)
    
    payment_mode = fields.Str(required=False)
    
    dp_details = fields.Nested(DPDetails, required=False)
    
    status = fields.Nested(ShipmentStatusData, required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    order = fields.Nested(OrderDetailsData, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    vertical = fields.Str(required=False)
    
    user_agent = fields.Str(required=False)
    
    total_items = fields.Int(required=False)
    
    priority_text = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    packaging_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    enable_dp_tracking = fields.Str(required=False)
    
    picked_date = fields.Str(required=False)
    
    delivery_details = fields.Nested(UserDetailsData, required=False)
    
    platform_logo = fields.Str(required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    tracking_list = fields.List(fields.Nested(TrackingList, required=False), required=False)
    
    billing_details = fields.Nested(UserDetailsData, required=False)
    


class ShipmentDetailsResponse(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(OrderDict, required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    is_validated = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class FilterInfoOption(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class FiltersInfo(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    options = fields.List(fields.Nested(FilterInfoOption, required=False), required=False)
    


class PaymentModeInfo(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    image = fields.List(fields.Str(required=False), required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    l3_category = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    department_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    


class BagUnit(BaseSchema):
    # Order swagger.json

    
    item = fields.Nested(Item, required=False)
    
    item_quantity = fields.Int(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    gst = fields.Nested(GST, required=False)
    
    shipment_id = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
    status = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    ordering_channel = fields.Str(required=False)
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    ops_status = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    actual_status = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class UserDataInfo(BaseSchema):
    # Order swagger.json

    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    avis_user_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class ShipmentItemFulFillingStore(BaseSchema):
    # Order swagger.json

    
    code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    total_bags_count = fields.Int(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    application = fields.Dict(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    channel = fields.Dict(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    sla = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    id = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    


class ShipmentInternalPlatformViewResponse(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    page = fields.Dict(required=False)
    
    items = fields.List(fields.Nested(ShipmentItem, required=False), required=False)
    
    applied_filters = fields.Dict(required=False)
    


class ShipmentPricesDataSet(BaseSchema):
    # Order swagger.json

    
    value_of_good = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    cashback = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    gst_fee = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    coupon_effective_discount = fields.Int(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    refund_credit = fields.Int(required=False)
    


class Shipment1(BaseSchema):
    # Order swagger.json

    
    shipment_status = fields.Str(required=False)
    
    rtd_done = fields.Str(required=False)
    
    total_items = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    prices = fields.Nested(ShipmentPricesDataSet, required=False)
    


class ManifestShipmentResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(Shipment1, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ErrorSchemaDataSet(BaseSchema):
    # Order swagger.json

    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentPricesDataInfo(BaseSchema):
    # Order swagger.json

    
    value_of_good = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    refund_amount = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    coupon_value = fields.Str(required=False)
    
    cashback = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    discount = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    refund_credit = fields.Int(required=False)
    


class ShipmentDataSet(BaseSchema):
    # Order swagger.json

    
    total_bags = fields.Int(required=False)
    
    value_of_good = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    shipment_status = fields.Dict(required=False)
    
    total_items = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    cashback = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    coupon_effective_discount = fields.Int(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    prices = fields.Nested(ShipmentPricesDataInfo, required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    refund_credit = fields.Int(required=False)
    


class UserDataSet(BaseSchema):
    # Order swagger.json

    
    email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    


class OrderDataSet(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentDataSet, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    order_created_time = fields.Str(required=False)
    
    user_info = fields.Nested(UserDataSet, required=False)
    


class OrderListingResponse(BaseSchema):
    # Order swagger.json

    
    orders = fields.List(fields.Nested(OrderDataSet, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class OrderErrorSchemaDataSet(BaseSchema):
    # Order swagger.json

    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class Options(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Int(required=False)
    


class MetricsCount(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    options = fields.List(fields.Nested(Options, required=False), required=False)
    
    value = fields.Int(required=False)
    
    key = fields.Str(required=False)
    


class MetricCountResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(MetricsCount, required=False), required=False)
    


class FiltersResponse(BaseSchema):
    # Order swagger.json

    
    channels = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    
    delivery_partners = fields.List(fields.Nested(FiltersInfo, required=False), required=False)
    


class Success(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class OmsReports(BaseSchema):
    # Order swagger.json

    
    report_created_at = fields.Str(required=False)
    
    report_requested_at = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    report_type = fields.Str(required=False)
    
    report_name = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    request_details = fields.Dict(required=False)
    
    s3_key = fields.Str(required=False)
    


class JioCodeUpsertDataSet(BaseSchema):
    # Order swagger.json

    
    item_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    jio_code = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    


class JioCodeUpsertPayload(BaseSchema):
    # Order swagger.json

    
    data = fields.List(fields.Nested(JioCodeUpsertDataSet, required=False), required=False)
    


class NestedErrorSchemaDataSet(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class JioCodeUpsertResponse(BaseSchema):
    # Order swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    error = fields.List(fields.Nested(NestedErrorSchemaDataSet, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    


class ProductDetail(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    


class ShipmentBody(BaseSchema):
    # Order swagger.json

    
    store_invoice_id = fields.Str(required=False)
    
    data_update = fields.Dict(required=False)
    
    reason = fields.List(fields.Int(required=False), required=False)
    
    bags = fields.List(fields.Int(required=False), required=False)
    
    products = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    


class ShipmentDetail(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Nested(ShipmentBody, required=False)
    


class Statuses(BaseSchema):
    # Order swagger.json

    
    exclude_bags_next_state = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    shipments = fields.Nested(ShipmentDetail, required=False)
    


class PlatformShipmentStatusInternal(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    
    statuses = fields.Nested(Statuses, required=False)
    


class ResponseDetail(BaseSchema):
    # Order swagger.json

    
    message = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ErrorDetail(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


class HistoryDict(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    l3_detail = fields.Str(required=False)
    
    l1_detail = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    createdat = fields.Str(required=False)
    
    ticket_id = fields.Str(required=False)
    
    ticket_url = fields.Str(required=False)
    
    l2_detail = fields.Str(required=False)
    


class ShipmentHistoryResponse(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.List(fields.Nested(HistoryDict, required=False), required=False)
    


class PlatformOrderUpdate(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    


