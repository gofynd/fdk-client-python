"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class UserInfo(BaseSchema):
    pass


class FulfillingStore(BaseSchema):
    pass


class PricesBreakup(BaseSchema):
    pass


class PaymentInfo(BaseSchema):
    pass


class FulfillingCompany(BaseSchema):
    pass


class ItemBrand(BaseSchema):
    pass


class Item(BaseSchema):
    pass


class CurrentStatus(BaseSchema):
    pass


class Prices(BaseSchema):
    pass


class BagsData(BaseSchema):
    pass


class ShipmentResponse(BaseSchema):
    pass


class ShipmentById(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class CustomerDetailsResponse(BaseSchema):
    pass


class SendOtpToCustomerResponse(BaseSchema):
    pass


class ShipmentReasonsResponse(BaseSchema):
    pass


class VerifyOtp(BaseSchema):
    pass


class VerifyOtpResponse(BaseSchema):
    pass


class OrderItems(BaseSchema):
    pass


class Statuses(BaseSchema):
    pass


class Filters(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class OrderList(BaseSchema):
    pass


class TrackShipmentResults(BaseSchema):
    pass


class TrackShipmentResponse(BaseSchema):
    pass


class ProductDetail(BaseSchema):
    pass


class ShipmentBody(BaseSchema):
    pass


class ShipmentDetail(BaseSchema):
    pass


class Statuses1(BaseSchema):
    pass


class ShipmentStatusUpdateBody(BaseSchema):
    pass


class ShipmentStatusUpdate(BaseSchema):
    pass


class ErrorDetail(BaseSchema):
    pass





class UserInfo(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class PricesBreakup(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    display = fields.Str(required=False)
    


class PaymentInfo(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    mop = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    


class FulfillingCompany(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class ItemBrand(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class Item(BaseSchema):
    # Order swagger.json

    
    image = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False)
    
    brand = fields.Nested(ItemBrand, required=False)
    
    size = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class CurrentStatus(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class Prices(BaseSchema):
    # Order swagger.json

    
    refund_credit = fields.Int(required=False)
    
    coupon_value = fields.Int(required=False)
    
    value_of_good = fields.Int(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    promotion_effective_discount = fields.Int(required=False)
    
    refund_amount = fields.Int(required=False)
    
    amount_paid = fields.Int(required=False)
    
    added_to_fynd_cash = fields.Int(required=False)
    
    cashback = fields.Int(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    transfer_price = fields.Int(required=False)
    
    cod_charges = fields.Int(required=False)
    
    pm_price_split = fields.Dict(required=False)
    
    price_marked = fields.Int(required=False)
    
    coupon_effective_discount = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    discount = fields.Int(required=False)
    


class BagsData(BaseSchema):
    # Order swagger.json

    
    can_return = fields.Boolean(required=False)
    
    item = fields.Nested(Item, required=False)
    
    current_status = fields.Nested(CurrentStatus, required=False)
    
    id = fields.Int(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    financial_breakup = fields.List(fields.Dict(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    


class ShipmentResponse(BaseSchema):
    # Order swagger.json

    
    order_id = fields.Str(required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    returnable_date = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    need_help_url = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    dp_name = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(PricesBreakup, required=False), required=False)
    
    size_info = fields.Dict(required=False)
    
    track_url = fields.Str(required=False)
    
    promise = fields.Dict(required=False)
    
    can_return = fields.Boolean(required=False)
    
    delivery_date = fields.Str(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    shipment_status = fields.Dict(required=False)
    
    total_bags = fields.Int(required=False)
    
    traking_no = fields.Str(required=False)
    
    tracking_details = fields.Dict(required=False)
    
    awb_no = fields.Str(required=False)
    
    invoice = fields.Dict(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    payment = fields.Nested(PaymentInfo, required=False)
    
    refund_details = fields.Dict(required=False)
    
    can_break = fields.Dict(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    total_details = fields.Dict(required=False)
    
    prices = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(BagsData, required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    


class ShipmentById(BaseSchema):
    # Order swagger.json

    
    shipment = fields.Nested(ShipmentResponse, required=False)
    


class Error(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


class CustomerDetailsResponse(BaseSchema):
    # Order swagger.json

    
    country = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class SendOtpToCustomerResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentReasonsResponse(BaseSchema):
    # Order swagger.json

    
    flow = fields.Str(required=False)
    
    feedback_type = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    reason_text = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    
    show_text_area = fields.Boolean(required=False)
    


class VerifyOtp(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    
    otp_code = fields.Int(required=False)
    


class VerifyOtpResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    


class OrderItems(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    order_created_time = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    user_info = fields.Dict(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    bags_for_reorder = fields.List(fields.Dict(required=False), required=False)
    


class Statuses(BaseSchema):
    # Order swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Int(required=False)
    
    display = fields.Str(required=False)
    


class Filters(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(Statuses, required=False), required=False)
    


class Page(BaseSchema):
    # Order swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class OrderList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    page = fields.Nested(Page, required=False)
    


class TrackShipmentResults(BaseSchema):
    # Order swagger.json

    
    account_name = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    


class TrackShipmentResponse(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(TrackShipmentResults, required=False), required=False)
    


class ProductDetail(BaseSchema):
    # Order swagger.json

    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class ShipmentBody(BaseSchema):
    # Order swagger.json

    
    reason = fields.List(fields.Int(required=False), required=False)
    
    store_invoice_id = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    bags = fields.List(fields.Int(required=False), required=False)
    
    data_update = fields.Dict(required=False)
    


class ShipmentDetail(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Nested(ShipmentBody, required=False)
    


class Statuses1(BaseSchema):
    # Order swagger.json

    
    exclude_bags_next_state = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    shipments = fields.Nested(ShipmentDetail, required=False)
    


class ShipmentStatusUpdateBody(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(Statuses1, required=False), required=False)
    
    task = fields.Boolean(required=False)
    
    force_transition = fields.Boolean(required=False)
    


class ShipmentStatusUpdate(BaseSchema):
    # Order swagger.json

    
    message = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ErrorDetail(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


