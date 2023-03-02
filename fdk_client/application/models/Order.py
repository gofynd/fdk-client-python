"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class OrderById(BaseSchema):
    pass


class OrderList(BaseSchema):
    pass


class OrderPage(BaseSchema):
    pass


class OrderFilters(BaseSchema):
    pass


class OrderStatuses(BaseSchema):
    pass


class ReqBodyVerifyOTPShipment(BaseSchema):
    pass


class ResponseGetCreditNoteShipment(BaseSchema):
    pass


class ResponseGetInvoiceShipment(BaseSchema):
    pass


class ResponseVerifyOTPShipment(BaseSchema):
    pass


class sendOTPApplicationResponse(BaseSchema):
    pass


class ShipmentBagReasons(BaseSchema):
    pass


class ShipmentById(BaseSchema):
    pass


class CustomerDetailsByShipmentId(BaseSchema):
    pass


class ShipmentReasons(BaseSchema):
    pass


class ShipmentStatusUpdateBody(BaseSchema):
    pass


class StatusesBody(BaseSchema):
    pass


class ShipmentStatusUpdate(BaseSchema):
    pass


class ShipmentTrack(BaseSchema):
    pass


class OrderSchema(BaseSchema):
    pass


class BagsForReorder(BaseSchema):
    pass


class BagsForReorderArticleAssignment(BaseSchema):
    pass


class PosOrderById(BaseSchema):
    pass


class BagReasons(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class FinancialBreakup(BaseSchema):
    pass


class Identifiers(BaseSchema):
    pass


class ItemBrand(BaseSchema):
    pass


class AppliedPromos(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class FreeGiftItemDetails(BaseSchema):
    pass


class ItemPriceDetails(BaseSchema):
    pass


class MarkedValues(BaseSchema):
    pass


class EffectiveValues(BaseSchema):
    pass


class BreakupValues(BaseSchema):
    pass


class DeliveryAddress(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class Invoice(BaseSchema):
    pass


class Promise(BaseSchema):
    pass


class Timestamp(BaseSchema):
    pass


class Reasons(BaseSchema):
    pass


class ShipmentStatus(BaseSchema):
    pass


class ShipmentUserInfo(BaseSchema):
    pass


class Shipments(BaseSchema):
    pass


class ShipmentTotalDetails(BaseSchema):
    pass


class ShipmentPayment(BaseSchema):
    pass


class Track(BaseSchema):
    pass


class TrackingDetails(BaseSchema):
    pass


class NestedTrackingDetails(BaseSchema):
    pass


class UserInfo(BaseSchema):
    pass


class ApefaceApiError(BaseSchema):
    pass



class OrderById(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(OrderSchema, required=False)
    


class OrderList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
    page = fields.Nested(OrderPage, required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    


class OrderPage(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class OrderFilters(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(OrderStatuses, required=False), required=False)
    


class OrderStatuses(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    


class ReqBodyVerifyOTPShipment(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    
    otp_code = fields.Str(required=False)
    


class ResponseGetCreditNoteShipment(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    


class ResponseGetInvoiceShipment(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    


class ResponseVerifyOTPShipment(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    


class sendOTPApplicationResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    


class ShipmentBagReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons, required=False), required=False)
    


class ShipmentById(BaseSchema):
    # Order swagger.json

    
    shipment = fields.Nested(Shipments, required=False)
    


class CustomerDetailsByShipmentId(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class ShipmentReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(Reasons, required=False), required=False)
    


class ShipmentStatusUpdateBody(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatusesBody, required=False), required=False)
    
    force_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    


class StatusesBody(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    shipments = fields.Dict(required=False)
    


class ShipmentStatusUpdate(BaseSchema):
    # Order swagger.json

    
    message = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Boolean(required=False)
    


class ShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(Track, required=False), required=False)
    


class OrderSchema(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    order_created_time = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    


class BagsForReorder(BaseSchema):
    # Order swagger.json

    
    item_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    


class BagsForReorderArticleAssignment(BaseSchema):
    # Order swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


class PosOrderById(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(OrderSchema, required=False)
    


class BagReasons(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    item = fields.Nested(Item, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    id = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    delivery_date = fields.Str(required=False)
    
    returnable_date = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    brand = fields.Nested(ItemBrand, required=False)
    
    name = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    id = fields.Float(required=False)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    amount_paid_roundoff = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    price_marked = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    


class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    


class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    brand_calculated_amount = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    total_units = fields.Int(required=False)
    
    discount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    identifiers = fields.Nested(Identifiers, required=False)
    
    gst_tag = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    item_name = fields.Str(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    


class Identifiers(BaseSchema):
    # Order swagger.json

    
    ean = fields.Str(required=False)
    
    sku_code = fields.Str(required=False)
    


class ItemBrand(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    amount = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    article_quantity = fields.Float(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    applied_free_articles = fields.Nested(AppliedFreeArticles, required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Float(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    free_gift_item_details = fields.List(fields.Nested(FreeGiftItemDetails, required=False), required=False)
    


class FreeGiftItemDetails(BaseSchema):
    # Order swagger.json

    
    item_id = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_price_details = fields.Nested(ItemPriceDetails, required=False)
    


class ItemPriceDetails(BaseSchema):
    # Order swagger.json

    
    currency = fields.Str(required=False)
    
    marked = fields.Nested(MarkedValues, required=False)
    
    effective = fields.Nested(EffectiveValues, required=False)
    


class MarkedValues(BaseSchema):
    # Order swagger.json

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class EffectiveValues(BaseSchema):
    # Order swagger.json

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class BreakupValues(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    name = fields.Str(required=False)
    


class DeliveryAddress(BaseSchema):
    # Order swagger.json

    
    pincode = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    email = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    code = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    company_name = fields.Str(required=False)
    


class Invoice(BaseSchema):
    # Order swagger.json

    
    updated_date = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    


class Promise(BaseSchema):
    # Order swagger.json

    
    show_promise = fields.Boolean(required=False)
    
    timestamp = fields.Nested(Timestamp, required=False)
    


class Timestamp(BaseSchema):
    # Order swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class Reasons(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    show_text_area = fields.Boolean(required=False)
    
    feedback_type = fields.Str(required=False)
    
    flow = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    
    priority = fields.Int(required=False)
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    


class ShipmentUserInfo(BaseSchema):
    # Order swagger.json

    
    gender = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    


class Shipments(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    track_url = fields.Str(required=False)
    
    traking_no = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    can_break = fields.Dict(required=False)
    
    delivery_date = fields.Str(required=False)
    
    returnable_date = fields.Str(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    need_help_url = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    comment = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Raw(required=False), required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    size_info = fields.Dict(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    


class ShipmentTotalDetails(BaseSchema):
    # Order swagger.json

    
    total_price = fields.Float(required=False)
    
    sizes = fields.Int(required=False)
    
    pieces = fields.Int(required=False)
    


class ShipmentPayment(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    mop = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class Track(BaseSchema):
    # Order swagger.json

    
    awb = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    account_name = fields.Str(required=False)
    


class TrackingDetails(BaseSchema):
    # Order swagger.json

    
    is_current = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    tracking_details = fields.List(fields.Nested(NestedTrackingDetails, required=False), required=False)
    


class NestedTrackingDetails(BaseSchema):
    # Order swagger.json

    
    is_current = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    


class UserInfo(BaseSchema):
    # Order swagger.json

    
    gender = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class ApefaceApiError(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


