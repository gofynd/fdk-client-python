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


class IntentAppErrorList(BaseSchema):
    pass


class PaymentModeLogo(BaseSchema):
    pass


class IntentApp(BaseSchema):
    pass


class PaymentModeList(BaseSchema):
    pass


class RootPaymentMode(BaseSchema):
    pass


class AggregatorRoute(BaseSchema):
    pass


class PaymentDefaultSelection(BaseSchema):
    pass


class PaymentFlow(BaseSchema):
    pass


class PaymentOptionAndFlow(BaseSchema):
    pass


class AdvanceObject(BaseSchema):
    pass


class SplitObject(BaseSchema):
    pass


class AdvancePaymentObject(BaseSchema):
    pass


class PaymentModeRouteResponse(BaseSchema):
    pass


class WalletLinkRequestSchema(BaseSchema):
    pass


class WalletVerifyRequestSchema(BaseSchema):
    pass


class WalletDelinkRequestSchema(BaseSchema):
    pass


class WalletResponseSchema(BaseSchema):
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


class CardDetails(BaseSchema):
    pass


class CardDetailsResponse(BaseSchema):
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


class KYCAddress(BaseSchema):
    pass


class UserPersonalInfoInDetails(BaseSchema):
    pass


class MarketplaceInfo(BaseSchema):
    pass


class BusinessDetails(BaseSchema):
    pass


class DeviceDetails(BaseSchema):
    pass


class CustomerOnboardingRequest(BaseSchema):
    pass


class OnboardSummary(BaseSchema):
    pass


class CustomerOnboardingResponse(BaseSchema):
    pass


class OutstandingOrderDetailsResponse(BaseSchema):
    pass


class PaidOrderDetailsResponse(BaseSchema):
    pass


class DeleteRefundAccountResponse(BaseSchema):
    pass


class RefundOptionsDetails(BaseSchema):
    pass


class RefundOptions(BaseSchema):
    pass


class OfflineRefundOptions(BaseSchema):
    pass


class RefundOptionResponse(BaseSchema):
    pass


class SelectedRefundOptionResponse(BaseSchema):
    pass


class WalletBeneficiaryDetails(BaseSchema):
    pass


class UpiBeneficiaryDetails(BaseSchema):
    pass


class BeneficiaryRefundOptions(BaseSchema):
    pass


class OrderBeneficiaryResponseSchemaV2(BaseSchema):
    pass


class ValidateValidateAddressRequest(BaseSchema):
    pass


class VPADetails(BaseSchema):
    pass


class ValidateValidateAddressResponse(BaseSchema):
    pass


class PaymentMethodsMetaOrder(BaseSchema):
    pass


class PaymentOrderMethods(BaseSchema):
    pass


class PaymentOrderRequest(BaseSchema):
    pass


class PaymentOrderData(BaseSchema):
    pass


class PaymentOrderResponse(BaseSchema):
    pass


class ShipmentRefundRequest(BaseSchema):
    pass


class ShipmentRefundDetail(BaseSchema):
    pass


class ShipmentRefundResponse(BaseSchema):
    pass





class AggregatorConfigDetail(BaseSchema):
    # Payment swagger.json

    
    sdk = fields.Boolean(required=False, allow_none=True)
    
    secret = fields.Str(required=False)
    
    api = fields.Str(required=False, allow_none=True)
    
    pin = fields.Str(required=False, allow_none=True)
    
    config_type = fields.Str(required=False)
    
    merchant_key = fields.Str(required=False, allow_none=True)
    
    verify_api = fields.Str(required=False, allow_none=True)
    
    key = fields.Str(required=False)
    
    user_id = fields.Str(required=False, allow_none=True)
    
    merchant_id = fields.Str(required=False, allow_none=True)
    


class AggregatorsConfigDetailResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    razorpay = fields.Nested(AggregatorConfigDetail, required=False)
    
    juspay = fields.Nested(AggregatorConfigDetail, required=False)
    
    simpl = fields.Nested(AggregatorConfigDetail, required=False)
    
    payumoney = fields.Nested(AggregatorConfigDetail, required=False)
    
    rupifi = fields.Nested(AggregatorConfigDetail, required=False)
    
    mswipe = fields.Nested(AggregatorConfigDetail, required=False)
    
    stripe = fields.Nested(AggregatorConfigDetail, required=False)
    
    ccavenue = fields.Nested(AggregatorConfigDetail, required=False)
    
    env = fields.Str(required=False)
    


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

    
    nickname = fields.Str(required=False)
    
    refresh = fields.Boolean(required=False, allow_none=True)
    
    card_id = fields.Str(required=False, allow_none=True)
    
    name_on_card = fields.Str(required=False)
    


class AttachCardsResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CardPaymentGateway(BaseSchema):
    # Payment swagger.json

    
    api = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False, allow_none=True)
    


class ActiveCardPaymentGatewayResponse(BaseSchema):
    # Payment swagger.json

    
    cards = fields.Nested(CardPaymentGateway, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Card(BaseSchema):
    # Payment swagger.json

    
    card_number = fields.Str(required=False, allow_none=True)
    
    card_name = fields.Str(required=False, allow_none=True)
    
    card_type = fields.Str(required=False, allow_none=True)
    
    card_brand_image = fields.Str(required=False, allow_none=True)
    
    card_reference = fields.Str(required=False, allow_none=True)
    
    card_issuer = fields.Str(required=False, allow_none=True)
    
    card_brand = fields.Str(required=False, allow_none=True)
    
    expired = fields.Boolean(required=False, allow_none=True)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False, allow_none=True)
    
    card_isin = fields.Str(required=False, allow_none=True)
    
    exp_year = fields.Int(required=False, allow_none=True)
    
    nickname = fields.Str(required=False, allow_none=True)
    
    aggregator_name = fields.Str(required=False)
    
    card_fingerprint = fields.Str(required=False, allow_none=True)
    
    card_token = fields.Str(required=False, allow_none=True)
    
    exp_month = fields.Int(required=False, allow_none=True)
    
    card_id = fields.Str(required=False, allow_none=True)
    


class ListCardsResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class DeletehCardRequest(BaseSchema):
    # Payment swagger.json

    
    card_id = fields.Str(required=False, allow_none=True)
    


class DeleteCardsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    phone_number = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    order_items = fields.List(fields.Dict(required=False), required=False)
    
    payload = fields.Str(required=False, allow_none=True)
    
    merchant_params = fields.Dict(required=False)
    
    delivery_address = fields.Dict(required=False)
    


class ValidateCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ChargeCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    verified = fields.Boolean(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    transaction_token = fields.Str(required=False, allow_none=True)
    
    amount = fields.Int(required=False, allow_none=True)
    


class ChargeCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    cart_id = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    delivery_address_id = fields.Str(required=False, allow_none=True)
    


class PaymentInitializationRequest(BaseSchema):
    # Payment swagger.json

    
    razorpay_payment_id = fields.Str(required=False, allow_none=True)
    
    method = fields.Str(required=False)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    amount = fields.Int(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    


class PaymentInitializationResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False, allow_none=True)
    
    aggregator_order_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    upi_poll_url = fields.Str(required=False, allow_none=True)
    
    virtual_id = fields.Str(required=False, allow_none=True)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    polling_url = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    customer_id = fields.Str(required=False, allow_none=True)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    currency = fields.Str(required=False, allow_none=True)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    amount = fields.Int(required=False, allow_none=True)
    
    bqr_image = fields.Str(required=False, allow_none=True)
    


class PaymentStatusUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    amount = fields.Int(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    


class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    retry = fields.Boolean(required=False)
    
    redirect_url = fields.Str(required=False, allow_none=True)
    
    aggregator_name = fields.Str(required=False)
    


class IntentAppErrorList(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False, allow_none=True)
    
    package_name = fields.Str(required=False, allow_none=True)
    


class PaymentModeLogo(BaseSchema):
    # Payment swagger.json

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    


class IntentApp(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False, allow_none=True)
    
    package_name = fields.Str(required=False, allow_none=True)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    display_name = fields.Str(required=False, allow_none=True)
    


class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    card_number = fields.Str(required=False, allow_none=True)
    
    merchant_code = fields.Str(required=False, allow_none=True)
    
    card_reference = fields.Str(required=False, allow_none=True)
    
    card_issuer = fields.Str(required=False, allow_none=True)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    cod_limit = fields.Float(required=False, allow_none=True)
    
    intent_flow = fields.Boolean(required=False, allow_none=True)
    
    fynd_vpa = fields.Str(required=False, allow_none=True)
    
    intent_app_error_dict_list = fields.List(fields.Nested(IntentAppErrorList, required=False), required=False)
    
    aggregator_name = fields.Str(required=False)
    
    card_fingerprint = fields.Str(required=False, allow_none=True)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    
    intent_app = fields.List(fields.Nested(IntentApp, required=False), required=False)
    
    expired = fields.Boolean(required=False, allow_none=True)
    
    retry_count = fields.Int(required=False, allow_none=True)
    
    exp_year = fields.Int(required=False, allow_none=True)
    
    exp_month = fields.Int(required=False, allow_none=True)
    
    card_id = fields.Str(required=False, allow_none=True)
    
    remaining_limit = fields.Float(required=False, allow_none=True)
    
    display_priority = fields.Int(required=False, allow_none=True)
    
    card_brand = fields.Str(required=False, allow_none=True)
    
    cod_limit_per_order = fields.Float(required=False, allow_none=True)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    nickname = fields.Str(required=False, allow_none=True)
    
    card_name = fields.Str(required=False, allow_none=True)
    
    card_type = fields.Str(required=False, allow_none=True)
    
    card_brand_image = fields.Str(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    card_isin = fields.Str(required=False, allow_none=True)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    card_token = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    


class RootPaymentMode(BaseSchema):
    # Payment swagger.json

    
    is_pay_by_card_pl = fields.Boolean(required=False, allow_none=True)
    
    add_card_enabled = fields.Boolean(required=False, allow_none=True)
    
    display_priority = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    save_card = fields.Boolean(required=False, allow_none=True)
    
    aggregator_name = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    anonymous_enable = fields.Boolean(required=False, allow_none=True)
    


class AggregatorRoute(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False, allow_none=True)
    
    payment_flow_data = fields.Str(required=False, allow_none=True)
    
    payment_flow = fields.Str(required=False, allow_none=True)
    
    api_link = fields.Str(required=False, allow_none=True)
    


class PaymentDefaultSelection(BaseSchema):
    # Payment swagger.json

    
    mode = fields.Str(required=False, allow_none=True)
    
    identifier = fields.Str(required=False, allow_none=True)
    
    skip = fields.Boolean(required=False, allow_none=True)
    


class PaymentFlow(BaseSchema):
    # Payment swagger.json

    
    bqr_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    fynd = fields.Nested(AggregatorRoute, required=False)
    
    epaylater = fields.Nested(AggregatorRoute, required=False)
    
    razorpay = fields.Nested(AggregatorRoute, required=False)
    
    juspay = fields.Nested(AggregatorRoute, required=False)
    
    ajiodhan = fields.Nested(AggregatorRoute, required=False)
    
    simpl = fields.Nested(AggregatorRoute, required=False)
    
    rupifi = fields.Nested(AggregatorRoute, required=False)
    
    mswipe = fields.Nested(AggregatorRoute, required=False)
    
    stripe = fields.Nested(AggregatorRoute, required=False)
    
    ccavenue = fields.Nested(AggregatorRoute, required=False)
    
    payubiz = fields.Nested(AggregatorRoute, required=False)
    
    jiopay = fields.Nested(AggregatorRoute, required=False)
    
    upi_razorpay = fields.Nested(AggregatorRoute, required=False)
    


class PaymentOptionAndFlow(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    
    payment_default_selection = fields.Nested(PaymentDefaultSelection, required=False)
    


class AdvanceObject(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    amount = fields.Float(required=False)
    
    time_unit = fields.Str(required=False, allow_none=True)
    
    description = fields.Str(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    prepayment_type = fields.Str(required=False, allow_none=True)
    
    prepayment_value = fields.Float(required=False, allow_none=True)
    
    cancellation_type = fields.Str(required=False, allow_none=True)
    
    refund_time_limit = fields.Float(required=False, allow_none=True)
    
    all_prepayment_type = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
    allow_custom_advance_amount = fields.Boolean(required=False, allow_none=True)
    


class SplitObject(BaseSchema):
    # Payment swagger.json

    
    total_number_of_splits = fields.Float(required=False, allow_none=True)
    
    splits_remaining = fields.Float(required=False, allow_none=True)
    
    amount_remaining = fields.Float(required=False, allow_none=True)
    


class AdvancePaymentObject(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False, allow_none=True)
    
    display_priority = fields.Float(required=False, allow_none=True)
    
    payment_mode_id = fields.Float(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    split = fields.Nested(SplitObject, required=False)
    
    advance = fields.Nested(AdvanceObject, required=False)
    


class PaymentModeRouteResponse(BaseSchema):
    # Payment swagger.json

    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    
    success = fields.Boolean(required=False)
    
    payment_breakup = fields.Dict(required=False)
    
    advance_payment = fields.List(fields.Nested(AdvancePaymentObject, required=False), required=False)
    


class WalletLinkRequestSchema(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    wallet_code = fields.Str(required=False)
    


class WalletVerifyRequestSchema(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    link_token = fields.Str(required=False)
    
    otp = fields.Int(required=False)
    


class WalletDelinkRequestSchema(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    wallet_code = fields.Str(required=False)
    


class WalletResponseSchema(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class RupifiBannerData(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    kyc_url = fields.Str(required=False)
    


class RupifiBannerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(RupifiBannerData, required=False)
    
    success = fields.Boolean(required=False)
    


class EpaylaterBannerData(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    display = fields.Boolean(required=False)
    


class EpaylaterBannerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EpaylaterBannerData, required=False)
    
    success = fields.Boolean(required=False)
    


class ResendOrCancelPaymentRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    request_type = fields.Str(required=False)
    


class LinkStatus(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ResendOrCancelPaymentResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(LinkStatus, required=False)
    
    success = fields.Boolean(required=False)
    


class renderHTMLRequest(BaseSchema):
    # Payment swagger.json

    
    returntype = fields.Str(required=False, allow_none=True)
    
    base64_html = fields.Str(required=False)
    


class renderHTMLResponse(BaseSchema):
    # Payment swagger.json

    
    html = fields.Str(required=False)
    


class ValidateVPARequest(BaseSchema):
    # Payment swagger.json

    
    upi_vpa = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    


class ValidateUPI(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    upi_vpa = fields.Str(required=False)
    


class ValidateVPAResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ValidateUPI, required=False)
    
    success = fields.Boolean(required=False)
    


class CardDetails(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    country = fields.Str(required=False)
    
    bank_code = fields.Str(required=False, allow_none=True)
    
    id = fields.Str(required=False)
    
    card_exp_year = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    card_sub_type = fields.Str(required=False, allow_none=True)
    
    is_domestic_card = fields.Boolean(required=False)
    
    name_on_card = fields.Str(required=False)
    
    card_exp_month = fields.Str(required=False)
    
    extended_card_type = fields.Str(required=False)
    
    card_object = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    bank = fields.Str(required=False)
    


class CardDetailsResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(CardDetails, required=False)
    
    success = fields.Boolean(required=False)
    


class TransferItemsDetails(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    logo_large = fields.Str(required=False)
    
    logo_small = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class TransferModeDetails(BaseSchema):
    # Payment swagger.json

    
    items = fields.List(fields.Nested(TransferItemsDetails, required=False), required=False)
    
    display_name = fields.Str(required=False)
    


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

    
    modified_on = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class OrderBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    


class NotFoundResourceError(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class IfscCodeResponse(BaseSchema):
    # Payment swagger.json

    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    bank_name = fields.Str(required=False)
    


class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class AddBeneficiaryViaOtpVerificationRequest(BaseSchema):
    # Payment swagger.json

    
    request_id = fields.Str(required=False)
    
    hash_key = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class AddBeneficiaryViaOtpVerificationResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class WrongOtpError(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    success = fields.Str(required=False)
    


class BeneficiaryModeDetails(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    branch_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    wallet = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    


class AddBeneficiaryDetailsRequest(BaseSchema):
    # Payment swagger.json

    
    delights = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    
    otp = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class RefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class BankDetailsForOTP(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    


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

    
    request_id = fields.Str(required=False)
    
    is_verified_flag = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class SetDefaultBeneficiaryRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    


class SetDefaultBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    is_beneficiary_set = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class GetPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    payment_link_current_status = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    payment_link_url = fields.Str(required=False, allow_none=True)
    
    external_order_id = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False)
    
    merchant_name = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    


class ErrorDescription(BaseSchema):
    # Payment swagger.json

    
    payment_transaction_id = fields.Str(required=False, allow_none=True)
    
    expired = fields.Boolean(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False, allow_none=True)
    
    merchant_name = fields.Str(required=False, allow_none=True)
    
    msg = fields.Str(required=False, allow_none=True)
    
    cancelled = fields.Boolean(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    
    invalid_id = fields.Boolean(required=False, allow_none=True)
    


class ErrorResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CreatePaymentLinkMeta(BaseSchema):
    # Payment swagger.json

    
    cart_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    assign_card_id = fields.Str(required=False, allow_none=True)
    
    amount = fields.Str(required=False)
    


class CreatePaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False, allow_none=True)
    
    external_order_id = fields.Str(required=False)
    
    mobile_number = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    email = fields.Str(required=False)
    


class CreatePaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    payment_link_url = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False, allow_none=True)
    


class CancelOrResendPaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    


class ResendPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CancelPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class PollingPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False, allow_none=True)
    
    status_code = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    http_status = fields.Int(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    redirect_url = fields.Str(required=False, allow_none=True)
    
    payment_link_id = fields.Str(required=False, allow_none=True)
    
    aggregator_name = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    


class PaymentMethodsMeta(BaseSchema):
    # Payment swagger.json

    
    merchant_code = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class CreateOrderUserPaymentMethods(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    meta = fields.Nested(PaymentMethodsMeta, required=False)
    


class CreateOrderUserRequest(BaseSchema):
    # Payment swagger.json

    
    failure_callback_url = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    payment_methods = fields.Nested(CreateOrderUserPaymentMethods, required=False)
    
    success_callback_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    


class CreateOrderUserData(BaseSchema):
    # Payment swagger.json

    
    method = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False, allow_none=True)
    
    customer_id = fields.Str(required=False, allow_none=True)
    
    contact = fields.Str(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    currency = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    


class CreateOrderUserResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(CreateOrderUserData, required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    payment_confirm_url = fields.Str(required=False, allow_none=True)
    


class BalanceDetails(BaseSchema):
    # Payment swagger.json

    
    formatted_value = fields.Str(required=False, allow_none=True)
    
    currency = fields.Str(required=False, allow_none=True)
    
    value = fields.Float(required=False, allow_none=True)
    


class CreditSummary(BaseSchema):
    # Payment swagger.json

    
    total_due_amount = fields.Nested(BalanceDetails, required=False)
    
    status = fields.Str(required=False, allow_none=True)
    
    limit = fields.Nested(BalanceDetails, required=False)
    
    credit_line_id = fields.Str(required=False, allow_none=True)
    
    amount_available = fields.Nested(BalanceDetails, required=False)
    
    due_amount = fields.Nested(BalanceDetails, required=False)
    
    due_date = fields.Str(required=False, allow_none=True)
    
    balance = fields.Nested(BalanceDetails, required=False)
    
    status_message = fields.Str(required=False, allow_none=True)
    
    repayment_url = fields.Str(required=False, allow_none=True)
    
    soa_url = fields.Str(required=False, allow_none=True)
    
    is_eligible_for_txn = fields.Boolean(required=False, allow_none=True)
    
    merchant_customer_ref_id = fields.Str(required=False, allow_none=True)
    
    buyer_status = fields.Str(required=False, allow_none=True)
    
    activation_url = fields.Str(required=False, allow_none=True)
    


class CustomerCreditSummaryResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(CreditSummary, required=False)
    
    success = fields.Boolean(required=False)
    


class RedirectURL(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    signup_url = fields.Str(required=False)
    


class RedirectToAggregatorResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(RedirectURL, required=False)
    
    success = fields.Boolean(required=False)
    


class CreditDetail(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    is_registered = fields.Boolean(required=False)
    
    signup_url = fields.Str(required=False)
    


class CheckCreditResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(CreditDetail, required=False)
    
    success = fields.Boolean(required=False)
    


class KYCAddress(BaseSchema):
    # Payment swagger.json

    
    city = fields.Str(required=False)
    
    addressline2 = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False)
    
    ownership_type = fields.Str(required=False, allow_none=True)
    
    pincode = fields.Str(required=False)
    
    land_mark = fields.Str(required=False, allow_none=True)
    
    addressline1 = fields.Str(required=False)
    


class UserPersonalInfoInDetails(BaseSchema):
    # Payment swagger.json

    
    first_name = fields.Str(required=False)
    
    voter_id = fields.Str(required=False, allow_none=True)
    
    gender = fields.Str(required=False, allow_none=True)
    
    dob = fields.Str(required=False, allow_none=True)
    
    passport = fields.Str(required=False, allow_none=True)
    
    fathers_name = fields.Str(required=False, allow_none=True)
    
    mothers_name = fields.Str(required=False, allow_none=True)
    
    middle_name = fields.Str(required=False, allow_none=True)
    
    last_name = fields.Str(required=False, allow_none=True)
    
    pan = fields.Str(required=False, allow_none=True)
    
    driving_license = fields.Str(required=False, allow_none=True)
    
    email_verified = fields.Boolean(required=False)
    
    address_as_per_id = fields.Nested(KYCAddress, required=False)
    
    mobile_verified = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    email = fields.Str(required=False, allow_none=True)
    


class MarketplaceInfo(BaseSchema):
    # Payment swagger.json

    
    date_of_joining = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    membership_id = fields.Str(required=False)
    


class BusinessDetails(BaseSchema):
    # Payment swagger.json

    
    business_ownership_type = fields.Str(required=False, allow_none=True)
    
    vintage = fields.Str(required=False, allow_none=True)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    pan = fields.Str(required=False, allow_none=True)
    
    entity_type = fields.Str(required=False, allow_none=True)
    
    shop_and_establishment = fields.Dict(required=False)
    
    fssai = fields.Str(required=False, allow_none=True)
    
    fda = fields.Str(required=False, allow_none=True)
    
    business_type = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    address = fields.Nested(KYCAddress, required=False)
    


class DeviceDetails(BaseSchema):
    # Payment swagger.json

    
    identification_number = fields.Str(required=False, allow_none=True)
    
    identifier_type = fields.Str(required=False, allow_none=True)
    
    device_model = fields.Str(required=False, allow_none=True)
    
    device_make = fields.Str(required=False, allow_none=True)
    
    device_type = fields.Str(required=False, allow_none=True)
    
    os = fields.Str(required=False, allow_none=True)
    
    os_version = fields.Str(required=False, allow_none=True)
    


class CustomerOnboardingRequest(BaseSchema):
    # Payment swagger.json

    
    personal_info = fields.Nested(UserPersonalInfoInDetails, required=False)
    
    mcc = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    marketplace_info = fields.Nested(MarketplaceInfo, required=False)
    
    source = fields.Str(required=False)
    
    business_info = fields.Nested(BusinessDetails, required=False)
    
    device = fields.Nested(DeviceDetails, required=False)
    


class OnboardSummary(BaseSchema):
    # Payment swagger.json

    
    redirect_url = fields.Str(required=False)
    
    session = fields.Dict(required=False)
    
    status = fields.Boolean(required=False)
    
    status_remark = fields.Str(required=False)
    
    is_eligible_for_txn = fields.Boolean(required=False)
    
    merchant_customer_ref_id = fields.Str(required=False)
    
    activation_url = fields.Str(required=False)
    


class CustomerOnboardingResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(OnboardSummary, required=False)
    
    success = fields.Boolean(required=False)
    


class OutstandingOrderDetailsResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class PaidOrderDetailsResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class DeleteRefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class RefundOptionsDetails(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    


class RefundOptions(BaseSchema):
    # Payment swagger.json

    
    items = fields.Nested(RefundOptionsDetails, required=False)
    


class OfflineRefundOptions(BaseSchema):
    # Payment swagger.json

    
    items = fields.Nested(RefundOptionsDetails, required=False)
    
    payment_modes = fields.List(fields.Str(required=False), required=False)
    


class RefundOptionResponse(BaseSchema):
    # Payment swagger.json

    
    offline_refund_options = fields.Nested(OfflineRefundOptions, required=False)
    
    success = fields.Boolean(required=False)
    
    refund_options = fields.Nested(RefundOptions, required=False)
    


class SelectedRefundOptionResponse(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Dict(required=False)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    


class WalletBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    beneficiary_id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    subtitle = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    wallet_address = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    wallet = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False, allow_none=True)
    


class UpiBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    beneficiary_id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    subtitle = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    vpa_address = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False, allow_none=True)
    


class BeneficiaryRefundOptions(BaseSchema):
    # Payment swagger.json

    
    bank = fields.Nested(OrderBeneficiaryDetails, required=False)
    
    wallet = fields.Nested(WalletBeneficiaryDetails, required=False)
    
    upi = fields.Nested(UpiBeneficiaryDetails, required=False)
    


class OrderBeneficiaryResponseSchemaV2(BaseSchema):
    # Payment swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    data = fields.Nested(BeneficiaryRefundOptions, required=False)
    
    limit = fields.Dict(required=False)
    


class ValidateValidateAddressRequest(BaseSchema):
    # Payment swagger.json

    
    ifsc_code = fields.Str(required=False, allow_none=True)
    
    upi_vpa = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False, allow_none=True)
    


class VPADetails(BaseSchema):
    # Payment swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    upi_vpa = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    


class ValidateValidateAddressResponse(BaseSchema):
    # Payment swagger.json

    
    upi = fields.Nested(VPADetails, required=False)
    
    success = fields.Boolean(required=False)
    
    ifsc = fields.Dict(required=False)
    


class PaymentMethodsMetaOrder(BaseSchema):
    # Payment swagger.json

    
    merchant_code = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class PaymentOrderMethods(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False)
    
    payment = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    meta = fields.Nested(PaymentMethodsMetaOrder, required=False)
    
    name = fields.Str(required=False)
    


class PaymentOrderRequest(BaseSchema):
    # Payment swagger.json

    
    payment_methods = fields.List(fields.Nested(PaymentOrderMethods, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    


class PaymentOrderData(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    customer_id = fields.Str(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False, allow_none=True)
    
    currency = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    contact = fields.Str(required=False, allow_none=True)
    
    method = fields.Str(required=False, allow_none=True)
    


class PaymentOrderResponse(BaseSchema):
    # Payment swagger.json

    
    payment_confirm_url = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    data = fields.Nested(PaymentOrderData, required=False)
    
    message = fields.Str(required=False)
    


class ShipmentRefundRequest(BaseSchema):
    # Payment swagger.json

    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False, allow_none=True)
    


class ShipmentRefundDetail(BaseSchema):
    # Payment swagger.json

    
    shipment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    


class ShipmentRefundResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ShipmentRefundDetail, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


