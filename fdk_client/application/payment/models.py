"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class AggregatorConfigDetail(BaseSchema):
    pass


class AggregatorsConfigDetailResponse(BaseSchema):
    pass


class ErrorCodeAndDescription(BaseSchema):
    pass


class HttpErrorCodeAndResponse(BaseSchema):
    pass


class AttachCardRequest(BaseSchema):
    pass


class AttachCardsResponse(BaseSchema):
    pass


class CardPaymentGateway(BaseSchema):
    pass


class ActiveCardPaymentGatewayResponse(BaseSchema):
    pass


class Card(BaseSchema):
    pass


class ListCardsResponse(BaseSchema):
    pass


class DeletehCardRequest(BaseSchema):
    pass


class DeleteCardsResponse(BaseSchema):
    pass


class ValidateCustomerRequest(BaseSchema):
    pass


class ValidateCustomerResponse(BaseSchema):
    pass


class ChargeCustomerRequest(BaseSchema):
    pass


class ChargeCustomerResponse(BaseSchema):
    pass


class PaymentInitializationRequest(BaseSchema):
    pass


class PaymentInitializationResponse(BaseSchema):
    pass


class PaymentStatusUpdateRequest(BaseSchema):
    pass


class PaymentStatusUpdateResponse(BaseSchema):
    pass


class AggregatorRoute(BaseSchema):
    pass


class PaymentFlow(BaseSchema):
    pass


class PaymentModeLogo(BaseSchema):
    pass


class PaymentModeList(BaseSchema):
    pass


class RootPaymentMode(BaseSchema):
    pass


class PaymentOptionAndFlow(BaseSchema):
    pass


class PaymentModeRouteResponse(BaseSchema):
    pass


class RupifiBannerData(BaseSchema):
    pass


class RupifiBannerResponse(BaseSchema):
    pass


class TransferItemsDetails(BaseSchema):
    pass


class TransferModeDetails(BaseSchema):
    pass


class TransferModeResponse(BaseSchema):
    pass


class UpdateRefundTransferModeRequest(BaseSchema):
    pass


class UpdateRefundTransferModeResponse(BaseSchema):
    pass


class OrderBeneficiaryDetails(BaseSchema):
    pass


class OrderBeneficiaryResponse(BaseSchema):
    pass


class NotFoundResourceError(BaseSchema):
    pass


class IfscCodeResponse(BaseSchema):
    pass


class ErrorCodeDescription(BaseSchema):
    pass


class AddBeneficiaryViaOtpVerificationRequest(BaseSchema):
    pass


class AddBeneficiaryViaOtpVerificationResponse(BaseSchema):
    pass


class WrongOtpError(BaseSchema):
    pass


class BeneficiaryModeDetails(BaseSchema):
    pass


class AddBeneficiaryDetailsRequest(BaseSchema):
    pass


class RefundAccountResponse(BaseSchema):
    pass


class BankDetailsForOTP(BaseSchema):
    pass


class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    pass


class WalletOtpRequest(BaseSchema):
    pass


class WalletOtpResponse(BaseSchema):
    pass


class SetDefaultBeneficiaryRequest(BaseSchema):
    pass


class SetDefaultBeneficiaryResponse(BaseSchema):
    pass





class AggregatorConfigDetail(BaseSchema):
    # Payment swagger.json

    
    config_type = fields.Str(required=False)
    
    merchant_key = fields.Str(required=False)
    
    pin = fields.Str(required=False)
    
    sdk = fields.Boolean(required=False)
    
    secret = fields.Str(required=False)
    
    verify_api = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    api = fields.Str(required=False)
    
    merchant_id = fields.Str(required=False)
    


class AggregatorsConfigDetailResponse(BaseSchema):
    # Payment swagger.json

    
    juspay = fields.Nested(AggregatorConfigDetail, required=False)
    
    payumoney = fields.Nested(AggregatorConfigDetail, required=False)
    
    ccavenue = fields.Nested(AggregatorConfigDetail, required=False)
    
    mswipe = fields.Nested(AggregatorConfigDetail, required=False)
    
    env = fields.Str(required=False)
    
    razorpay = fields.Nested(AggregatorConfigDetail, required=False)
    
    simpl = fields.Nested(AggregatorConfigDetail, required=False)
    
    stripe = fields.Nested(AggregatorConfigDetail, required=False)
    
    success = fields.Boolean(required=False)
    
    rupifi = fields.Nested(AggregatorConfigDetail, required=False)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class HttpErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    


class AttachCardRequest(BaseSchema):
    # Payment swagger.json

    
    card_id = fields.Str(required=False)
    
    refresh = fields.Boolean(required=False)
    
    name_on_card = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    


class AttachCardsResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class CardPaymentGateway(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    api = fields.Str(required=False)
    


class ActiveCardPaymentGatewayResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    cards = fields.Nested(CardPaymentGateway, required=False)
    
    success = fields.Boolean(required=False)
    


class Card(BaseSchema):
    # Payment swagger.json

    
    card_issuer = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    card_number = fields.Str(required=False)
    
    card_reference = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    card_isin = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    
    card_name = fields.Str(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    card_type = fields.Str(required=False)
    
    exp_year = fields.Int(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    exp_month = fields.Int(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    


class ListCardsResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class DeletehCardRequest(BaseSchema):
    # Payment swagger.json

    
    card_id = fields.Str(required=False)
    


class DeleteCardsResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    transaction_amount_in_paise = fields.Int(required=False)
    
    phone_number = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    merchant_params = fields.Dict(required=False)
    
    payload = fields.Str(required=False)
    


class ValidateCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class ChargeCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    verified = fields.Boolean(required=False)
    
    amount = fields.Int(required=False)
    
    transaction_token = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class ChargeCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    delivery_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentInitializationRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    virtual_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    polling_url = fields.Str(required=False)
    


class PaymentInitializationResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    virtual_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    bqr_image = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    amount = fields.Int(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    polling_url = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentStatusUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    retry = fields.Boolean(required=False)
    


class AggregatorRoute(BaseSchema):
    # Payment swagger.json

    
    payment_flow = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    api_link = fields.Str(required=False)
    


class PaymentFlow(BaseSchema):
    # Payment swagger.json

    
    juspay = fields.Nested(AggregatorRoute, required=False)
    
    payubiz = fields.Nested(AggregatorRoute, required=False)
    
    ccavenue = fields.Nested(AggregatorRoute, required=False)
    
    mswipe = fields.Nested(AggregatorRoute, required=False)
    
    fynd = fields.Nested(AggregatorRoute, required=False)
    
    razorpay = fields.Nested(AggregatorRoute, required=False)
    
    upi_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    simpl = fields.Nested(AggregatorRoute, required=False)
    
    stripe = fields.Nested(AggregatorRoute, required=False)
    
    bqr_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    rupifi = fields.Nested(AggregatorRoute, required=False)
    


class PaymentModeLogo(BaseSchema):
    # Payment swagger.json

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    


class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    merchant_code = fields.Str(required=False)
    
    fynd_vpa = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    intent_flow = fields.Boolean(required=False)
    
    exp_month = fields.Int(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    retry_count = fields.Int(required=False)
    
    expired = fields.Boolean(required=False)
    
    card_issuer = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    card_name = fields.Str(required=False)
    
    card_isin = fields.Str(required=False)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    
    card_number = fields.Str(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    card_type = fields.Str(required=False)
    
    exp_year = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    card_reference = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    card_fingerprint = fields.Str(required=False)
    


class RootPaymentMode(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    display_priority = fields.Int(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    


class PaymentOptionAndFlow(BaseSchema):
    # Payment swagger.json

    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    


class PaymentModeRouteResponse(BaseSchema):
    # Payment swagger.json

    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    
    success = fields.Boolean(required=False)
    


class RupifiBannerData(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    kyc_url = fields.Str(required=False)
    


class RupifiBannerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(RupifiBannerData, required=False)
    
    success = fields.Boolean(required=False)
    


class TransferItemsDetails(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Boolean(required=False)
    
    logo_large = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo_small = fields.Str(required=False)
    


class TransferModeDetails(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    items = fields.List(fields.Nested(TransferItemsDetails, required=False), required=False)
    


class TransferModeResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(TransferModeDetails, required=False), required=False)
    


class UpdateRefundTransferModeRequest(BaseSchema):
    # Payment swagger.json

    
    enable = fields.Boolean(required=False)
    
    transfer_mode = fields.Str(required=False)
    


class UpdateRefundTransferModeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    


class OrderBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    account_holder = fields.Str(required=False)
    
    comment = fields.Boolean(required=False)
    
    account_no = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    mobile = fields.Boolean(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    branch_name = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    


class OrderBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    


class NotFoundResourceError(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    


class IfscCodeResponse(BaseSchema):
    # Payment swagger.json

    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    bank_name = fields.Str(required=False)
    


class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    


class AddBeneficiaryViaOtpVerificationRequest(BaseSchema):
    # Payment swagger.json

    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
    hash_key = fields.Str(required=False)
    


class AddBeneficiaryViaOtpVerificationResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class WrongOtpError(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class BeneficiaryModeDetails(BaseSchema):
    # Payment swagger.json

    
    account_holder = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    wallet = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    


class AddBeneficiaryDetailsRequest(BaseSchema):
    # Payment swagger.json

    
    shipment_id = fields.Str(required=False)
    
    delights = fields.Boolean(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    
    otp = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class RefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class BankDetailsForOTP(BaseSchema):
    # Payment swagger.json

    
    account_holder = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    


class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    


class WalletOtpRequest(BaseSchema):
    # Payment swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class WalletOtpResponse(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class SetDefaultBeneficiaryRequest(BaseSchema):
    # Payment swagger.json

    
    beneficiary_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class SetDefaultBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    is_beneficiary_set = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


