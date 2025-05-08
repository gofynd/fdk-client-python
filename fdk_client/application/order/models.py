"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class OrderPage(BaseSchema):
    pass


class UserInfo(BaseSchema):
    pass


class BreakupValues(BaseSchema):
    pass


class ShipmentPayment(BaseSchema):
    pass


class ShipmentPaymentInfo(BaseSchema):
    pass


class ShipmentUserInfo(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class ChargeDistributionSchema(BaseSchema):
    pass


class ChargeDistributionLogic(BaseSchema):
    pass


class ChargeAmountCurrency(BaseSchema):
    pass


class ChargeAmount(BaseSchema):
    pass


class PriceAdjustmentCharge(BaseSchema):
    pass


class ShipmentStatus(BaseSchema):
    pass


class Invoice(BaseSchema):
    pass


class NestedTrackingDetails(BaseSchema):
    pass


class TrackingDetails(BaseSchema):
    pass


class TimeStampData(BaseSchema):
    pass


class Promise(BaseSchema):
    pass


class ShipmentTotalDetails(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class ItemBrand(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class AppliedFreeArticles(BaseSchema):
    pass


class AppliedPromos(BaseSchema):
    pass


class Identifiers(BaseSchema):
    pass


class FinancialBreakup(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class FulfillingCompany(BaseSchema):
    pass


class Article(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class CouponDetails(BaseSchema):
    pass


class Shipments(BaseSchema):
    pass


class BagsForReorderArticleAssignment(BaseSchema):
    pass


class BagsForReorder(BaseSchema):
    pass


class CurrencySchema(BaseSchema):
    pass


class OrderSchema(BaseSchema):
    pass


class OrderStatuses(BaseSchema):
    pass


class OrderGlobalFilterOption(BaseSchema):
    pass


class OrderGlobalFilter(BaseSchema):
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


class CustomerDetailsResponseSchema(BaseSchema):
    pass


class SendOtpToCustomerResponseSchema(BaseSchema):
    pass


class VerifyOtp(BaseSchema):
    pass


class VerifyOtpResponseSchema(BaseSchema):
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


class ProductsReasonsData(BaseSchema):
    pass


class ProductsReasonsFilters(BaseSchema):
    pass


class ProductsReasons(BaseSchema):
    pass


class EntityReasonData(BaseSchema):
    pass


class EntitiesReasons(BaseSchema):
    pass


class ReasonsData(BaseSchema):
    pass


class Products(BaseSchema):
    pass


class ProductsDataUpdatesFilters(BaseSchema):
    pass


class ProductsDataUpdates(BaseSchema):
    pass


class EntitiesDataUpdates(BaseSchema):
    pass


class DataUpdates(BaseSchema):
    pass


class ShipmentsRequestSchema(BaseSchema):
    pass


class StatuesRequestSchema(BaseSchema):
    pass


class OrderRequestSchema(BaseSchema):
    pass


class UpdateShipmentStatusRequestSchema(BaseSchema):
    pass


class StatusesBodyResponseSchema(BaseSchema):
    pass


class ShipmentApplicationStatusResponseSchema(BaseSchema):
    pass


class ErrorResponseSchema(BaseSchema):
    pass





class OrderPage(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class UserInfo(BaseSchema):
    # Order swagger.json

    
    first_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class BreakupValues(BaseSchema):
    # Order swagger.json

    
    value = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class ShipmentPayment(BaseSchema):
    # Order swagger.json

    
    mop = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class ShipmentPaymentInfo(BaseSchema):
    # Order swagger.json

    
    mop = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    


class ShipmentUserInfo(BaseSchema):
    # Order swagger.json

    
    first_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class ChargeDistributionSchema(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    logic = fields.Str(required=False)
    


class ChargeDistributionLogic(BaseSchema):
    # Order swagger.json

    
    distribution = fields.Nested(ChargeDistributionSchema, required=False)
    
    distribution_level = fields.Str(required=False)
    


class ChargeAmountCurrency(BaseSchema):
    # Order swagger.json

    
    value = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class ChargeAmount(BaseSchema):
    # Order swagger.json

    
    base_currency = fields.Nested(ChargeAmountCurrency, required=False)
    
    ordering_currency = fields.Nested(ChargeAmountCurrency, required=False)
    


class PriceAdjustmentCharge(BaseSchema):
    # Order swagger.json

    
    code = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False, allow_none=True)
    
    amount = fields.Nested(ChargeAmount, required=False)
    
    distribution_logic = fields.Nested(ChargeDistributionLogic, required=False)
    


class ShipmentStatus(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False, allow_none=True)
    
    title = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    


class Invoice(BaseSchema):
    # Order swagger.json

    
    invoice_url = fields.Str(required=False)
    
    updated_date = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    


class NestedTrackingDetails(BaseSchema):
    # Order swagger.json

    
    is_passed = fields.Boolean(required=False)
    
    time = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    


class TrackingDetails(BaseSchema):
    # Order swagger.json

    
    value = fields.Str(required=False, allow_none=True)
    
    is_current = fields.Boolean(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    created_ts = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(NestedTrackingDetails, required=False), required=False)
    


class TimeStampData(BaseSchema):
    # Order swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class Promise(BaseSchema):
    # Order swagger.json

    
    show_promise = fields.Boolean(required=False)
    
    timestamp = fields.Nested(TimeStampData, required=False)
    


class ShipmentTotalDetails(BaseSchema):
    # Order swagger.json

    
    pieces = fields.Int(required=False)
    
    total_price = fields.Float(required=False)
    
    sizes = fields.Int(required=False)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    delivery_charge = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    transfer_price = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    amount_to_be_collected = fields.Float(required=False)
    


class ItemBrand(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    image = fields.List(fields.Str(required=False), required=False)
    
    l1_categories = fields.List(fields.Str(required=False), required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    l2_category_id = fields.Float(required=False)
    
    brand = fields.Nested(ItemBrand, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    id = fields.Float(required=False)
    
    name = fields.Str(required=False)
    
    l3_category_name = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    l2_categories = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    


class AppliedFreeArticles(BaseSchema):
    # Order swagger.json

    
    article_id = fields.Str(required=False)
    
    free_gift_item_details = fields.Dict(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    mrp_promotion = fields.Boolean(required=False)
    
    promotion_name = fields.Str(required=False)
    
    article_quantity = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    promotion_type = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticles, required=False), required=False)
    


class Identifiers(BaseSchema):
    # Order swagger.json

    
    ean = fields.Str(required=False)
    
    sku_code = fields.Str(required=False)
    


class FinancialBreakup(BaseSchema):
    # Order swagger.json

    
    coupon_value = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    transfer_price = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    total_units = fields.Int(required=False)
    
    identifiers = fields.Nested(Identifiers, required=False)
    
    gst_tag = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    amount_to_be_collected = fields.Float(required=False)
    


class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    journey_type = fields.Str(required=False, allow_none=True)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    delivery_date = fields.Str(required=False, allow_none=True)
    
    line_number = fields.Int(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    item = fields.Nested(Item, required=False)
    
    applied_promos = fields.List(fields.Nested(AppliedPromos, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    returnable_date = fields.Str(required=False, allow_none=True)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    currency_code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    article = fields.Nested(Article, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    


class FulfillingCompany(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class Article(BaseSchema):
    # Order swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    


class Address(BaseSchema):
    # Order swagger.json

    
    pincode = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    latitude = fields.Float(required=False, allow_none=True)
    
    address2 = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    longitude = fields.Float(required=False, allow_none=True)
    
    country_iso_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    display_address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class CouponDetails(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class Shipments(BaseSchema):
    # Order swagger.json

    
    coupon_details = fields.List(fields.Nested(CouponDetails, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    payment_info = fields.List(fields.Nested(ShipmentPaymentInfo, required=False), required=False)
    
    order_type = fields.Str(required=False, allow_none=True)
    
    gstin_code = fields.Str(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    shipment_id = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    comment = fields.Str(required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    refund_details = fields.Dict(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    can_break = fields.Dict(required=False)
    
    traking_no = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    total_bags = fields.Int(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    returnable_date = fields.Str(required=False, allow_none=True)
    
    shipment_created_at = fields.Str(required=False)
    
    shipment_created_ts = fields.Str(required=False)
    
    size_info = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    dp_name = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    can_return = fields.Boolean(required=False)
    
    delivery_address = fields.Nested(Address, required=False)
    
    billing_address = fields.Nested(Address, required=False)
    
    track_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    need_help_url = fields.Str(required=False)
    
    return_meta = fields.Dict(required=False)
    
    delivery_date = fields.Str(required=False, allow_none=True)
    
    order = fields.Nested(OrderRequestSchema, required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    


class BagsForReorderArticleAssignment(BaseSchema):
    # Order swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    


class BagsForReorder(BaseSchema):
    # Order swagger.json

    
    item_size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    article_assignment = fields.Nested(BagsForReorderArticleAssignment, required=False)
    
    seller_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    


class CurrencySchema(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class OrderSchema(BaseSchema):
    # Order swagger.json

    
    coupon_details = fields.List(fields.Nested(CouponDetails, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    gstin_code = fields.Str(required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    order_created_time = fields.Str(required=False)
    
    order_created_ts = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
    charges = fields.List(fields.Nested(PriceAdjustmentCharge, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    currency = fields.Nested(CurrencySchema, required=False)
    
    custom_json = fields.Dict(required=False, allow_none=True)
    


class OrderStatuses(BaseSchema):
    # Order swagger.json

    
    value = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    


class OrderGlobalFilterOption(BaseSchema):
    # Order swagger.json

    
    display_text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    


class OrderGlobalFilter(BaseSchema):
    # Order swagger.json

    
    display_test = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(OrderGlobalFilterOption, required=False), required=False)
    


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
    
    success = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    


class Track(BaseSchema):
    # Order swagger.json

    
    account_name = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class ShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(Track, required=False), required=False)
    


class CustomerDetailsResponseSchema(BaseSchema):
    # Order swagger.json

    
    phone = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class SendOtpToCustomerResponseSchema(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    resend_timer = fields.Int(required=False)
    


class VerifyOtp(BaseSchema):
    # Order swagger.json

    
    otp_code = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class VerifyOtpResponseSchema(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class BagReasonMeta(BaseSchema):
    # Order swagger.json

    
    show_text_area = fields.Boolean(required=False)
    


class QuestionSet(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class BagReasons(BaseSchema):
    # Order swagger.json

    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Nested(BagReasonMeta, required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    reasons = fields.List(fields.Nested(lambda: BagReasons(exclude=('reasons')), required=False), required=False)
    


class ShipmentBagReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    rule_id = fields.Int(required=False, allow_none=True)
    


class ShipmentReason(BaseSchema):
    # Order swagger.json

    
    priority = fields.Int(required=False)
    
    show_text_area = fields.Boolean(required=False)
    
    reason_id = fields.Int(required=False)
    
    feedback_type = fields.Str(required=False)
    
    reason_text = fields.Str(required=False)
    
    flow = fields.Str(required=False)
    


class ShipmentReasons(BaseSchema):
    # Order swagger.json

    
    reasons = fields.List(fields.Nested(ShipmentReason, required=False), required=False)
    


class ProductsReasonsData(BaseSchema):
    # Order swagger.json

    
    reason_id = fields.Int(required=False)
    
    reason_text = fields.Str(required=False)
    


class ProductsReasonsFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    


class ProductsReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(ProductsReasonsData, required=False)
    
    filters = fields.List(fields.Nested(ProductsReasonsFilters, required=False), required=False)
    


class EntityReasonData(BaseSchema):
    # Order swagger.json

    
    reason_id = fields.Int(required=False)
    
    reason_text = fields.Str(required=False)
    


class EntitiesReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(EntityReasonData, required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    


class ReasonsData(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(ProductsReasons, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesReasons, required=False), required=False)
    


class Products(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    


class ProductsDataUpdatesFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class ProductsDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters, required=False), required=False)
    


class EntitiesDataUpdates(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    


class DataUpdates(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    


class ShipmentsRequestSchema(BaseSchema):
    # Order swagger.json

    
    reasons = fields.Nested(ReasonsData, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    identifier = fields.Str(required=False)
    


class StatuesRequestSchema(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentsRequestSchema, required=False), required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class OrderRequestSchema(BaseSchema):
    # Order swagger.json

    
    meta = fields.Dict(required=False)
    


class UpdateShipmentStatusRequestSchema(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatuesRequestSchema, required=False), required=False)
    
    task = fields.Boolean(required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    force_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    


class StatusesBodyResponseSchema(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Dict(required=False), required=False)
    


class ShipmentApplicationStatusResponseSchema(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatusesBodyResponseSchema, required=False), required=False)
    


class ErrorResponseSchema(BaseSchema):
    # Order swagger.json

    
    code = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    status = fields.Int(required=False)
    
    exception = fields.Str(required=False, allow_none=True)
    
    stack_trace = fields.Str(required=False, allow_none=True)
    


