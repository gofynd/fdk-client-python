"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class OrderPage(BaseSchema):
    pass


class NestedTrackingDetails(BaseSchema):
    pass


class TrackingDetails(BaseSchema):
    pass


class BreakupValues(BaseSchema):
    pass


class FulfillingCompany(BaseSchema):
    pass


class ItemBrand(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class AppliedPromos(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class Identifiers(BaseSchema):
    pass


class FinancialBreakup(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class DeliveryAddress(BaseSchema):
    pass


class ShipmentPayment(BaseSchema):
    pass


class Invoice(BaseSchema):
    pass


class ShipmentUserInfo(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class TimeStampData(BaseSchema):
    pass


class Promise(BaseSchema):
    pass


class ShipmentTotalDetails(BaseSchema):
    pass


class ShipmentStatus(BaseSchema):
    pass


class Shipments(BaseSchema):
    pass


class BagsForReorderArticleAssignment(BaseSchema):
    pass


class BagsForReorder(BaseSchema):
    pass


class UserInfo(BaseSchema):
    pass


class OrderSchema(BaseSchema):
    pass


class OrderStatuses(BaseSchema):
    pass


class OrderFilters(BaseSchema):
    pass


class OrderList(BaseSchema):
    pass


class ApefaceApiError(BaseSchema):
    pass


class OrderById(BaseSchema):
    pass


class ShipmentById(BaseSchema):
    pass


class ResponseGetInvoiceShipment(BaseSchema):
    pass


class Track(BaseSchema):
    pass


class ShipmentTrack(BaseSchema):
    pass


class CustomerDetailsResponse(BaseSchema):
    pass


class SendOtpToCustomerResponse(BaseSchema):
    pass


class VerifyOtp(BaseSchema):
    pass


class VerifyOtpResponse(BaseSchema):
    pass


class QuestionSet(BaseSchema):
    pass


class BagReasonMeta(BaseSchema):
    pass


class BagReasons(BaseSchema):
    pass


class ShipmentBagReasons(BaseSchema):
    pass


class ShipmentReason(BaseSchema):
    pass


class ShipmentReasons(BaseSchema):
    pass


class ShipmentStatusUpdateBody(BaseSchema):
    pass


class ShipmentStatusUpdate(BaseSchema):
    pass



class OrderPage(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class NestedTrackingDetails(BaseSchema):
    # Order swagger.json

    
    is_current = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    time = fields.Str(required=False)
    


class TrackingDetails(BaseSchema):
    # Order swagger.json

    
    tracking_details = fields.List(fields.Nested(NestedTrackingDetails, required=False), required=False)
    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    
    is_passed = fields.Boolean(required=False)
    


class BreakupValues(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class FulfillingCompany(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ItemBrand(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    id = fields.Float(required=False)
    
    brand = fields.Nested(ItemBrand, required=False)
    
    code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    slug_key = fields.Str(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Float(required=False)
    
    free_gift_item_details = fields.Dict(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    amount = fields.Float(required=False)
    
    article_quantity = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    promotion_name = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    


class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    


class Identifiers(BaseSchema):
    # Order swagger.json

    
    sku_code = fields.Str(required=False)
    
    ean = fields.Str(required=False)
    


class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    refund_credit = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    identifiers = fields.Nested(Identifiers, required=False)
    
    delivery_charge = fields.Float(required=False)
    
    total_units = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    item_name = fields.Str(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    gst_fee = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    refund_credit = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    item = fields.Nested(Item, required=False)
    
    id = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    delivery_date = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    returnable_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    


class DeliveryAddress(BaseSchema):
    # Order swagger.json

    
    latitude = fields.Float(required=False)
    
    version = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    state = fields.Str(required=False)
    


class ShipmentPayment(BaseSchema):
    # Order swagger.json

    
    display_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    mop = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class Invoice(BaseSchema):
    # Order swagger.json

    
    label_url = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    updated_date = fields.Str(required=False)
    


class ShipmentUserInfo(BaseSchema):
    # Order swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class TimeStampData(BaseSchema):
    # Order swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    


class Promise(BaseSchema):
    # Order swagger.json

    
    show_promise = fields.Boolean(required=False)
    
    timestamp = fields.Nested(TimeStampData, required=False)
    


class ShipmentTotalDetails(BaseSchema):
    # Order swagger.json

    
    pieces = fields.Int(required=False)
    
    sizes = fields.Int(required=False)
    
    total_price = fields.Float(required=False)
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    hex_code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class Shipments(BaseSchema):
    # Order swagger.json

    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    track_url = fields.Str(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    size_info = fields.Dict(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    delivery_date = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    returnable_date = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    awb_no = fields.Str(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    refund_details = fields.Dict(required=False)
    
    traking_no = fields.Str(required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    need_help_url = fields.Str(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    can_break = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    


class BagsForReorderArticleAssignment(BaseSchema):
    # Order swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    


class BagsForReorder(BaseSchema):
    # Order swagger.json

    
    item_id = fields.Int(required=False)
    
    seller_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    


class UserInfo(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    


class OrderSchema(BaseSchema):
    # Order swagger.json

    
    order_created_time = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    


class OrderStatuses(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Int(required=False)
    


class OrderFilters(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(OrderStatuses, required=False), required=False)
    


class OrderList(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(OrderPage, required=False)
    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    


class ApefaceApiError(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class OrderById(BaseSchema):
    # Order swagger.json

    
    order = fields.Nested(OrderSchema, required=False)
    


class ShipmentById(BaseSchema):
    # Order swagger.json

    
    shipment = fields.Nested(Shipments, required=False)
    


class ResponseGetInvoiceShipment(BaseSchema):
    # Order swagger.json

    
    presigned_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class Track(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    account_name = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    


class ShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(Track, required=False), required=False)
    


class CustomerDetailsResponse(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class SendOtpToCustomerResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    


class VerifyOtp(BaseSchema):
    # Order swagger.json

    
    otp_code = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class VerifyOtpResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    


class QuestionSet(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class BagReasonMeta(BaseSchema):
    # Order swagger.json

    
    show_text_area = fields.Boolean(required=False)
    


class BagReasons(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    reasons = fields.List(fields.Nested(lambda: BagReasons(exclude=('reasons')), required=False), required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    meta = fields.Nested(BagReasonMeta, required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    


class ShipmentBagReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentReason(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    feedback_type = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    
    flow = fields.Str(required=False)
    
    show_text_area = fields.Boolean(required=False)
    


class ShipmentReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(ShipmentReason, required=False), required=False)
    


class ShipmentStatusUpdateBody(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Dict(required=False), required=False)
    


class ShipmentStatusUpdate(BaseSchema):
    # Order swagger.json

    
    message = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Boolean(required=False)
    
    final_state = fields.Dict(required=False)
    

