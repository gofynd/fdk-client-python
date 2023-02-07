"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



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


class PaymentModeLogo(BaseSchema):
    pass


class IntentApp(BaseSchema):
    pass


class IntentAppErrorList(BaseSchema):
    pass


class PaymentModeList(BaseSchema):
    pass


class RootPaymentMode(BaseSchema):
    pass


class AggregatorRoute(BaseSchema):
    pass


class PaymentFlow(BaseSchema):
    pass


class PaymentOptionAndFlow(BaseSchema):
    pass


class PaymentModeRouteResponse(BaseSchema):
    pass


class RupifiBannerData(BaseSchema):
    pass


class RupifiBannerResponse(BaseSchema):
    pass


class EpaylaterBannerData(BaseSchema):
    pass


class EpaylaterBannerResponse(BaseSchema):
    pass


class ResendOrCancelPaymentRequest(BaseSchema):
    pass


class LinkStatus(BaseSchema):
    pass


class ResendOrCancelPaymentResponse(BaseSchema):
    pass


class renderHTMLRequest(BaseSchema):
    pass


class renderHTMLResponse(BaseSchema):
    pass


class ValidateVPARequest(BaseSchema):
    pass


class ValidateUPI(BaseSchema):
    pass


class ValidateVPAResponse(BaseSchema):
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


class GetPaymentLinkResponse(BaseSchema):
    pass


class ErrorDescription(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class CreatePaymentLinkMeta(BaseSchema):
    pass


class CreatePaymentLinkRequest(BaseSchema):
    pass


class CreatePaymentLinkResponse(BaseSchema):
    pass


class CancelOrResendPaymentLinkRequest(BaseSchema):
    pass


class ResendPaymentLinkResponse(BaseSchema):
    pass


class CancelPaymentLinkResponse(BaseSchema):
    pass


class PollingPaymentLinkResponse(BaseSchema):
    pass


class PaymentMethodsMeta(BaseSchema):
    pass


class CreateOrderUserPaymentMethods(BaseSchema):
    pass


class CreateOrderUserRequest(BaseSchema):
    pass


class CreateOrderUserData(BaseSchema):
    pass


class CreateOrderUserResponse(BaseSchema):
    pass


class BalanceDetails(BaseSchema):
    pass


class CreditSummary(BaseSchema):
    pass


class CustomerCreditSummaryResponse(BaseSchema):
    pass


class RedirectURL(BaseSchema):
    pass


class RedirectToAggregatorResponse(BaseSchema):
    pass


class CreditDetail(BaseSchema):
    pass


class CheckCreditResponse(BaseSchema):
    pass


class DeviceDetails(BaseSchema):
    pass


class KYCAddress(BaseSchema):
    pass


class UserPersonalInfoInDetails(BaseSchema):
    pass


class BusinessDetails(BaseSchema):
    pass


class MarketplaceInfo(BaseSchema):
    pass


class CustomerOnboardingRequest(BaseSchema):
    pass


class OnboardSummary(BaseSchema):
    pass


class CustomerOnboardingResponse(BaseSchema):
    pass



class AggregatorConfigDetail(BaseSchema):
    # Payment swagger.json

    
    pin = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    verify_api = fields.Str(required=False)
    
    sdk = fields.Boolean(required=False)
    
    api = fields.Str(required=False)
    
    merchant_id = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    merchant_key = fields.Str(required=False)
    


class AggregatorsConfigDetailResponse(BaseSchema):
    # Payment swagger.json

    
    simpl = fields.Nested(AggregatorConfigDetail, required=False)
    
    juspay = fields.Nested(AggregatorConfigDetail, required=False)
    
    success = fields.Boolean(required=False)
    
    env = fields.Str(required=False)
    
    payumoney = fields.Nested(AggregatorConfigDetail, required=False)
    
    ccavenue = fields.Nested(AggregatorConfigDetail, required=False)
    
    razorpay = fields.Nested(AggregatorConfigDetail, required=False)
    
    stripe = fields.Nested(AggregatorConfigDetail, required=False)
    
    mswipe = fields.Nested(AggregatorConfigDetail, required=False)
    
    rupifi = fields.Nested(AggregatorConfigDetail, required=False)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class HttpErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    


class AttachCardRequest(BaseSchema):
    # Payment swagger.json

    
    nickname = fields.Str(required=False)
    
    refresh = fields.Boolean(required=False)
    
    card_id = fields.Str(required=False)
    
    name_on_card = fields.Str(required=False)
    


class AttachCardsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    


class CardPaymentGateway(BaseSchema):
    # Payment swagger.json

    
    customer_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    api = fields.Str(required=False)
    


class ActiveCardPaymentGatewayResponse(BaseSchema):
    # Payment swagger.json

    
    cards = fields.Nested(CardPaymentGateway, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Card(BaseSchema):
    # Payment swagger.json

    
    exp_month = fields.Int(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    card_number = fields.Str(required=False)
    
    card_reference = fields.Str(required=False)
    
    card_issuer = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    exp_year = fields.Int(required=False)
    
    card_name = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    
    card_isin = fields.Str(required=False)
    
    card_type = fields.Str(required=False)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    


class ListCardsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
    message = fields.Str(required=False)
    


class DeletehCardRequest(BaseSchema):
    # Payment swagger.json

    
    card_id = fields.Str(required=False)
    


class DeleteCardsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    order_items = fields.List(fields.Dict(required=False), required=False)
    
    aggregator = fields.Str(required=False)
    
    payload = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    merchant_params = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    


class ValidateCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
    error = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    


class ChargeCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    amount = fields.Int(required=False)
    
    transaction_token = fields.Str(required=False)
    


class ChargeCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    delivery_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class PaymentInitializationRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    vpa = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    device_id = fields.Str(required=False)
    


class PaymentInitializationResponse(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    polling_url = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    upi_poll_url = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    vpa = fields.Str(required=False)
    
    bqr_image = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    virtual_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class PaymentStatusUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    vpa = fields.Str(required=False)
    
    device_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    retry = fields.Boolean(required=False)
    
    redirect_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class PaymentModeLogo(BaseSchema):
    # Payment swagger.json

    
    small = fields.Str(required=False)
    
    large = fields.Str(required=False)
    


class IntentApp(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    package_name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    


class IntentAppErrorList(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    package_name = fields.Str(required=False)
    


class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    intent_flow = fields.Boolean(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    retry_count = fields.Int(required=False)
    
    card_isin = fields.Str(required=False)
    
    intent_app = fields.List(fields.Nested(IntentApp, required=False), required=False)
    
    nickname = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    card_reference = fields.Str(required=False)
    
    cod_limit = fields.Float(required=False)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    
    display_priority = fields.Int(required=False)
    
    cod_limit_per_order = fields.Float(required=False)
    
    card_brand = fields.Str(required=False)
    
    card_issuer = fields.Str(required=False)
    
    intent_app_error_dict_list = fields.List(fields.Nested(IntentAppErrorList, required=False), required=False)
    
    card_name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False)
    
    fynd_vpa = fields.Str(required=False)
    
    exp_month = fields.Int(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    card_number = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    
    remaining_limit = fields.Float(required=False)
    
    exp_year = fields.Int(required=False)
    
    card_type = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class RootPaymentMode(BaseSchema):
    # Payment swagger.json

    
    is_pay_by_card_pl = fields.Boolean(required=False)
    
    save_card = fields.Boolean(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    


class AggregatorRoute(BaseSchema):
    # Payment swagger.json

    
    api_link = fields.Str(required=False)
    
    payment_flow = fields.Str(required=False)
    
    payment_flow_data = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    


class PaymentFlow(BaseSchema):
    # Payment swagger.json

    
    simpl = fields.Nested(AggregatorRoute, required=False)
    
    juspay = fields.Nested(AggregatorRoute, required=False)
    
    payubiz = fields.Nested(AggregatorRoute, required=False)
    
    epaylater = fields.Nested(AggregatorRoute, required=False)
    
    ccavenue = fields.Nested(AggregatorRoute, required=False)
    
    bqr_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    razorpay = fields.Nested(AggregatorRoute, required=False)
    
    jiopay = fields.Nested(AggregatorRoute, required=False)
    
    stripe = fields.Nested(AggregatorRoute, required=False)
    
    upi_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    mswipe = fields.Nested(AggregatorRoute, required=False)
    
    fynd = fields.Nested(AggregatorRoute, required=False)
    
    rupifi = fields.Nested(AggregatorRoute, required=False)
    


class PaymentOptionAndFlow(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    


class PaymentModeRouteResponse(BaseSchema):
    # Payment swagger.json

    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    
    success = fields.Boolean(required=False)
    


class RupifiBannerData(BaseSchema):
    # Payment swagger.json

    
    kyc_url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class RupifiBannerResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(RupifiBannerData, required=False)
    


class EpaylaterBannerData(BaseSchema):
    # Payment swagger.json

    
    display = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class EpaylaterBannerResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(EpaylaterBannerData, required=False)
    


class ResendOrCancelPaymentRequest(BaseSchema):
    # Payment swagger.json

    
    device_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    request_type = fields.Str(required=False)
    


class LinkStatus(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ResendOrCancelPaymentResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(LinkStatus, required=False)
    


class renderHTMLRequest(BaseSchema):
    # Payment swagger.json

    
    base64_html = fields.Str(required=False)
    
    returntype = fields.Str(required=False)
    


class renderHTMLResponse(BaseSchema):
    # Payment swagger.json

    
    html = fields.Str(required=False)
    


class ValidateVPARequest(BaseSchema):
    # Payment swagger.json

    
    upi_vpa = fields.Str(required=False)
    


class ValidateUPI(BaseSchema):
    # Payment swagger.json

    
    upi_vpa = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    


class ValidateVPAResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ValidateUPI, required=False)
    


class TransferItemsDetails(BaseSchema):
    # Payment swagger.json

    
    logo_small = fields.Str(required=False)
    
    logo_large = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class TransferModeDetails(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    items = fields.List(fields.Nested(TransferItemsDetails, required=False), required=False)
    


class TransferModeResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(TransferModeDetails, required=False), required=False)
    


class UpdateRefundTransferModeRequest(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Str(required=False)
    
    enable = fields.Boolean(required=False)
    


class UpdateRefundTransferModeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    


class OrderBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    address = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    branch_name = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    


class OrderBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    


class NotFoundResourceError(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class IfscCodeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    branch_name = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    


class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class AddBeneficiaryViaOtpVerificationRequest(BaseSchema):
    # Payment swagger.json

    
    otp = fields.Str(required=False)
    
    hash_key = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class AddBeneficiaryViaOtpVerificationResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class WrongOtpError(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class BeneficiaryModeDetails(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    wallet = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    


class AddBeneficiaryDetailsRequest(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    
    delights = fields.Boolean(required=False)
    


class RefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    


class BankDetailsForOTP(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    


class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    


class WalletOtpRequest(BaseSchema):
    # Payment swagger.json

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class WalletOtpResponse(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    


class SetDefaultBeneficiaryRequest(BaseSchema):
    # Payment swagger.json

    
    beneficiary_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class SetDefaultBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    is_beneficiary_set = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class GetPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    payment_link_url = fields.Str(required=False)
    
    external_order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    payment_link_current_status = fields.Str(required=False)
    
    polling_timeout = fields.Int(required=False)
    
    amount = fields.Float(required=False)
    
    merchant_name = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    


class ErrorDescription(BaseSchema):
    # Payment swagger.json

    
    msg = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    
    payment_transaction_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    invalid_id = fields.Boolean(required=False)
    
    cancelled = fields.Boolean(required=False)
    
    merchant_name = fields.Str(required=False)
    


class ErrorResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    
    message = fields.Str(required=False)
    


class CreatePaymentLinkMeta(BaseSchema):
    # Payment swagger.json

    
    checkout_mode = fields.Str(required=False)
    
    assign_card_id = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class CreatePaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    external_order_id = fields.Str(required=False)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    email = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    mobile_number = fields.Str(required=False)
    


class CreatePaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    payment_link_url = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    polling_timeout = fields.Int(required=False)
    
    status_code = fields.Int(required=False)
    


class CancelOrResendPaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    


class ResendPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    polling_timeout = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class CancelPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class PollingPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    
    http_status = fields.Int(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    status = fields.Str(required=False)
    


class PaymentMethodsMeta(BaseSchema):
    # Payment swagger.json

    
    payment_gateway = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class CreateOrderUserPaymentMethods(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    meta = fields.Nested(PaymentMethodsMeta, required=False)
    
    mode = fields.Str(required=False)
    


class CreateOrderUserRequest(BaseSchema):
    # Payment swagger.json

    
    meta = fields.Dict(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    failure_callback_url = fields.Str(required=False)
    
    success_callback_url = fields.Str(required=False)
    
    payment_methods = fields.Nested(CreateOrderUserPaymentMethods, required=False)
    


class CreateOrderUserData(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    callback_url = fields.Str(required=False)
    


class CreateOrderUserResponse(BaseSchema):
    # Payment swagger.json

    
    callback_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CreateOrderUserData, required=False)
    
    status_code = fields.Int(required=False)
    


class BalanceDetails(BaseSchema):
    # Payment swagger.json

    
    currency = fields.Str(required=False)
    
    formatted_value = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class CreditSummary(BaseSchema):
    # Payment swagger.json

    
    balance = fields.Nested(BalanceDetails, required=False)
    
    status_message = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    merchant_customer_ref_id = fields.Str(required=False)
    


class CustomerCreditSummaryResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CreditSummary, required=False)
    


class RedirectURL(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    signup_url = fields.Str(required=False)
    


class RedirectToAggregatorResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(RedirectURL, required=False)
    


class CreditDetail(BaseSchema):
    # Payment swagger.json

    
    is_registered = fields.Boolean(required=False)
    
    status = fields.Boolean(required=False)
    
    signup_url = fields.Str(required=False)
    


class CheckCreditResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CreditDetail, required=False)
    


class DeviceDetails(BaseSchema):
    # Payment swagger.json

    
    device_make = fields.Str(required=False)
    
    device_type = fields.Str(required=False)
    
    os = fields.Str(required=False)
    
    device_model = fields.Str(required=False)
    
    identification_number = fields.Str(required=False)
    
    identifier_type = fields.Str(required=False)
    
    os_version = fields.Str(required=False)
    


class KYCAddress(BaseSchema):
    # Payment swagger.json

    
    state = fields.Str(required=False)
    
    ownership_type = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    addressline2 = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    addressline1 = fields.Str(required=False)
    
    land_mark = fields.Str(required=False)
    


class UserPersonalInfoInDetails(BaseSchema):
    # Payment swagger.json

    
    address_as_per_id = fields.Nested(KYCAddress, required=False)
    
    gender = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile_verified = fields.Boolean(required=False)
    
    passport = fields.Str(required=False)
    
    dob = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    driving_license = fields.Str(required=False)
    
    voter_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    pan = fields.Str(required=False)
    
    fathers_name = fields.Str(required=False)
    
    mothers_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    email_verified = fields.Boolean(required=False)
    
    middle_name = fields.Str(required=False)
    


class BusinessDetails(BaseSchema):
    # Payment swagger.json

    
    entity_type = fields.Str(required=False)
    
    vintage = fields.Str(required=False)
    
    fda = fields.Str(required=False)
    
    address = fields.Nested(KYCAddress, required=False)
    
    gstin = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    pan = fields.Str(required=False)
    
    business_ownership_type = fields.Str(required=False)
    
    fssai = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    shop_and_establishment = fields.Dict(required=False)
    


class MarketplaceInfo(BaseSchema):
    # Payment swagger.json

    
    date_of_joining = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    membership_id = fields.Str(required=False)
    


class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    
    mcc = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    


class OnboardSummary(BaseSchema):
    # Payment swagger.json

    
    redirect_url = fields.Str(required=False)
    
    session = fields.Dict(required=False)
    
    status = fields.Boolean(required=False)
    


class CustomerOnboardingResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(OnboardSummary, required=False)
    


