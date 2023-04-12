"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class UserInfo(BaseSchema):
    pass


class BagsForReorderArticleAssignment(BaseSchema):
    pass


class BagsForReorder(BaseSchema):
    pass


class BreakupValues(BaseSchema):
    pass


class NestedTrackingDetails(BaseSchema):
    pass


class TrackingDetails(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class ShipmentStatus(BaseSchema):
    pass


class ShipmentTotalDetails(BaseSchema):
    pass


class Invoice(BaseSchema):
    pass


class ShipmentPayment(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class ShipmentUserInfo(BaseSchema):
    pass


class ItemBrand(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class Identifiers(BaseSchema):
    pass


class FinancialBreakup(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class AppliedPromos(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class TimeStampData(BaseSchema):
    pass


class Promise(BaseSchema):
    pass


class FulfillingCompany(BaseSchema):
    pass


class DeliveryAddress(BaseSchema):
    pass


class Shipments(BaseSchema):
    pass


class OrderSchema(BaseSchema):
    pass


class OrderStatuses(BaseSchema):
    pass


class OrderFilters(BaseSchema):
    pass


class OrderPage(BaseSchema):
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


class BagReasonMeta(BaseSchema):
    pass


class QuestionSet(BaseSchema):
    pass


class BagReasons(BaseSchema):
    pass


class ShipmentBagReasons(BaseSchema):
    pass


class ShipmentReason(BaseSchema):
    pass


class ShipmentReasons(BaseSchema):
    pass


class EntityReasonData(BaseSchema):
    pass


class EntitiesReasons(BaseSchema):
    pass


class ProductsReasonsData(BaseSchema):
    pass


class ProductsReasonsFilters(BaseSchema):
    pass


class ProductsReasons(BaseSchema):
    pass


class ReasonsData(BaseSchema):
    pass


class Products(BaseSchema):
    pass


class EntitiesDataUpdates(BaseSchema):
    pass


class ProductsDataUpdatesFilters(BaseSchema):
    pass


class ProductsDataUpdates(BaseSchema):
    pass


class DataUpdates(BaseSchema):
    pass


class ShipmentsRequest(BaseSchema):
    pass


class StatuesRequest(BaseSchema):
    pass


class UpdateShipmentStatusRequest(BaseSchema):
    pass


class StatusesBodyResponse(BaseSchema):
    pass


class ShipmentApplicationStatusResponse(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass





class UserInfo(BaseSchema):
    # Order swagger.json

    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class BagsForReorderArticleAssignment(BaseSchema):
    # Order swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


class BagsForReorder(BaseSchema):
    # Order swagger.json

    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    item_size = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    


class BreakupValues(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    display = fields.Str(required=False)
    


class NestedTrackingDetails(BaseSchema):
    # Order swagger.json

    
    time = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    


class TrackingDetails(BaseSchema):
    # Order swagger.json

    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(NestedTrackingDetails, required=False), required=False)
    
    is_current = fields.Boolean(required=False)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    


class ShipmentTotalDetails(BaseSchema):
    # Order swagger.json

    
    sizes = fields.Int(required=False)
    
    pieces = fields.Int(required=False)
    
    total_price = fields.Float(required=False)
    


class Invoice(BaseSchema):
    # Order swagger.json

    
    updated_date = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    


class ShipmentPayment(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    mop = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    fynd_credits = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    coupon_value = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    


class ShipmentUserInfo(BaseSchema):
    # Order swagger.json

    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class ItemBrand(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    image = fields.List(fields.Str(required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    brand = fields.Nested(ItemBrand, required=False)
    
    size = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    id = fields.Float(required=False)
    


class Identifiers(BaseSchema):
    # Order swagger.json

    
    sku_code = fields.Str(required=False)
    
    ean = fields.Str(required=False)
    


class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    fynd_credits = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    transfer_price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    coupon_value = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    cashback = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    identifiers = fields.Nested(Identifiers, required=False)
    
    total_units = fields.Int(required=False)
    
    refund_amount = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    item_name = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Order swagger.json

    
    article_id = fields.Str(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    free_gift_item_details = fields.Dict(required=False)
    
    quantity = fields.Float(required=False)
    


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    promotion_type = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    article_quantity = fields.Float(required=False)
    
    promotion_name = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    
    amount = fields.Float(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    


class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    journey_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    item = fields.Nested(Item, required=False)
    
    can_return = fields.Boolean(required=False)
    
    delivery_date = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    returnable_date = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class TimeStampData(BaseSchema):
    # Order swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    


class Promise(BaseSchema):
    # Order swagger.json

    
    timestamp = fields.Nested(TimeStampData, required=False)
    
    show_promise = fields.Boolean(required=False)
    


class FulfillingCompany(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class DeliveryAddress(BaseSchema):
    # Order swagger.json

    
    address = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    city = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class Shipments(BaseSchema):
    # Order swagger.json

    
    total_bags = fields.Int(required=False)
    
    comment = fields.Str(required=False)
    
    need_help_url = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    can_return = fields.Boolean(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    shipment_id = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    traking_no = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    can_break = fields.Dict(required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    refund_details = fields.Dict(required=False)
    
    delivery_date = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    returnable_date = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    size_info = fields.Dict(required=False)
    
    dp_name = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    track_url = fields.Str(required=False)
    


class OrderSchema(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    order_created_time = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    


class OrderStatuses(BaseSchema):
    # Order swagger.json

    
    value = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    


class OrderFilters(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(OrderStatuses, required=False), required=False)
    


class OrderPage(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class OrderList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    
    page = fields.Nested(OrderPage, required=False)
    


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

    
    presigned_url = fields.Str(required=False)
    
    presigned_type = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    


class Track(BaseSchema):
    # Order swagger.json

    
    awb = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    account_name = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    


class ShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(Track, required=False), required=False)
    


class CustomerDetailsResponse(BaseSchema):
    # Order swagger.json

    
    country = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class SendOtpToCustomerResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class VerifyOtp(BaseSchema):
    # Order swagger.json

    
    otp_code = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class VerifyOtpResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    


class BagReasonMeta(BaseSchema):
    # Order swagger.json

    
    show_text_area = fields.Boolean(required=False)
    


class QuestionSet(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class BagReasons(BaseSchema):
    # Order swagger.json

    
    meta = fields.Nested(BagReasonMeta, required=False)
    
    display_name = fields.Str(required=False)
    
    reasons = fields.List(fields.Nested(lambda: BagReasons(exclude=('reasons')), required=False), required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    id = fields.Int(required=False)
    


class ShipmentBagReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentReason(BaseSchema):
    # Order swagger.json

    
    show_text_area = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    feedback_type = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    
    flow = fields.Str(required=False)
    
    reason_text = fields.Str(required=False)
    


class ShipmentReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(ShipmentReason, required=False), required=False)
    


class EntityReasonData(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    


class EntitiesReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(EntityReasonData, required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    


class ProductsReasonsData(BaseSchema):
    # Order swagger.json

    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    


class ProductsReasonsFilters(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class ProductsReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(ProductsReasonsData, required=False)
    
    filters = fields.List(fields.Nested(ProductsReasonsFilters, required=False), required=False)
    


class ReasonsData(BaseSchema):
    # Order swagger.json

    
    entities = fields.List(fields.Nested(EntitiesReasons, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsReasons, required=False), required=False)
    


class Products(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class EntitiesDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    


class ProductsDataUpdatesFilters(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    


class ProductsDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters, required=False), required=False)
    


class DataUpdates(BaseSchema):
    # Order swagger.json

    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    


class ShipmentsRequest(BaseSchema):
    # Order swagger.json

    
    reasons = fields.Nested(ReasonsData, required=False)
    
    identifier = fields.Str(required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    


class StatuesRequest(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentsRequest, required=False), required=False)
    
    status = fields.Str(required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    


class UpdateShipmentStatusRequest(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatuesRequest, required=False), required=False)
    
    force_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    


class StatusesBodyResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Dict(required=False), required=False)
    


class ShipmentApplicationStatusResponse(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatusesBodyResponse, required=False), required=False)
    


class ErrorResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    exception = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    


