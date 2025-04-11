"""Payment Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema




class SubPaymentMode(BaseSchema):
    pass


class PaymentMethod(BaseSchema):
    pass


class Logos(BaseSchema):
    pass


class SessionPath(BaseSchema):
    pass


class RequiredSessionPath(BaseSchema):
    pass


class CheckoutType(BaseSchema):
    pass


class Mode(BaseSchema):
    pass


class Country(BaseSchema):
    pass


class Currency(BaseSchema):
    pass


class RefundTo(BaseSchema):
    pass


class PaymentConfigDetails(BaseSchema):
    pass


class PostPayoutDetails(BaseSchema):
    pass


class PostPayout(BaseSchema):
    pass


class Users(BaseSchema):
    pass


class BankDetails(BaseSchema):
    pass


class Payouts(BaseSchema):
    pass


class ErrorCodeAndDescription(BaseSchema):
    pass


class HttpErrorCodeAndMessage(BaseSchema):
    pass


class PayoutDetails(BaseSchema):
    pass


class MoreAttributes(BaseSchema):
    pass


class Customers(BaseSchema):
    pass


class PayoutsAggregator(BaseSchema):
    pass


class PayoutItem(BaseSchema):
    pass





class SubPaymentMode(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class PaymentMethod(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    sub_payment_mode = fields.List(fields.Nested(SubPaymentMode, required=False), required=False)
    
    name = fields.Str(required=False)
    
    logos = fields.Nested(Logos, required=False)
    
    slug = fields.Str(required=False)
    


class Logos(BaseSchema):
    # Payment swagger.json

    
    small = fields.Str(required=False)
    
    large = fields.Str(required=False)
    


class SessionPath(BaseSchema):
    # Payment swagger.json

    
    type = fields.Str(required=False)
    
    uri_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    methods = fields.List(fields.Str(required=False), required=False)
    


class RequiredSessionPath(BaseSchema):
    # Payment swagger.json

    
    version = fields.Str(required=False)
    
    paths = fields.List(fields.Nested(SessionPath, required=False), required=False)
    


class CheckoutType(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class Mode(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class Country(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class Currency(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class RefundTo(BaseSchema):
    # Payment swagger.json

    
    source = fields.Str(required=False)
    
    others = fields.Str(required=False)
    


class PaymentConfigDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    refund_to = fields.Nested(RefundTo, required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    
    required_session_paths = fields.List(fields.Nested(RequiredSessionPath, required=False), required=False)
    
    checkout_type = fields.List(fields.Nested(CheckoutType, required=False), required=False)
    
    auto_capture = fields.List(fields.Boolean(required=False), required=False)
    
    mode = fields.List(fields.Nested(Mode, required=False), required=False)
    
    country = fields.List(fields.Nested(Country, required=False), required=False)
    
    currency = fields.List(fields.Nested(Currency, required=False), required=False)
    


class PostPayoutDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    users = fields.Nested(Users, required=False)
    
    is_active = fields.Boolean(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    transfer_type = fields.Str(required=False)
    
    bank_details = fields.Nested(BankDetails, required=False)
    
    created = fields.Boolean(required=False)
    
    payouts = fields.Nested(Payouts, required=False)
    
    payment_status = fields.Str(required=False)
    
    updated = fields.Boolean(required=False)
    


class PostPayout(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    users = fields.Nested(Users, required=False)
    
    is_active = fields.Boolean(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    transfer_type = fields.Str(required=False)
    
    bank_details = fields.Nested(BankDetails, required=False)
    
    created = fields.Boolean(required=False)
    
    payouts = fields.Nested(Payouts, required=False)
    
    payment_status = fields.Str(required=False)
    
    updated = fields.Boolean(required=False)
    


class Users(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class BankDetails(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    


class Payouts(BaseSchema):
    # Payment swagger.json

    
    aggregator_fund_id = fields.Str(required=False, allow_none=True)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class HttpErrorCodeAndMessage(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    


class PayoutDetails(BaseSchema):
    # Payment swagger.json

    
    items = fields.List(fields.Nested(PayoutItem, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class MoreAttributes(BaseSchema):
    # Payment swagger.json

    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    


class Customers(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    unique_external_id = fields.Str(required=False)
    


class PayoutsAggregator(BaseSchema):
    # Payment swagger.json

    
    payout_details_id = fields.Int(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    aggregator_fund_id = fields.Str(required=False, allow_none=True)
    


class PayoutItem(BaseSchema):
    # Payment swagger.json

    
    unique_transfer_no = fields.Str(required=False)
    
    more_attributes = fields.Nested(MoreAttributes, required=False)
    
    transfer_type = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    customers = fields.Nested(Customers, required=False)
    
    payouts_aggregators = fields.List(fields.Nested(PayoutsAggregator, required=False), required=False)
    


