"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class AggregatorConfigDetail(BaseSchema):
    pass


class AggregatorsConfigDetail(BaseSchema):
    pass


class ErrorCodeAndDescription(BaseSchema):
    pass


class HttpErrorCodeAndResponseSchema(BaseSchema):
    pass


class HttpErrorCodeDetails(BaseSchema):
    pass


class AttachCard(BaseSchema):
    pass


class AttachCardsDetails(BaseSchema):
    pass


class CardPaymentGateway(BaseSchema):
    pass


class ActiveCardPaymentGatewayDetails(BaseSchema):
    pass


class Card(BaseSchema):
    pass


class ListCardsDetails(BaseSchema):
    pass


class DeleteCard(BaseSchema):
    pass


class DeleteCardsDetails(BaseSchema):
    pass


class ValidateCustomer(BaseSchema):
    pass


class ValidateCustomerDetails(BaseSchema):
    pass


class ChargeCustomer(BaseSchema):
    pass


class ChargeCustomerDetails(BaseSchema):
    pass


class PaymentInitialization(BaseSchema):
    pass


class PaymentInitializationDetails(BaseSchema):
    pass


class PaymentStatusUpdate(BaseSchema):
    pass


class PaymentStatusUpdateDetails(BaseSchema):
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


class SupportedMethodDetails(BaseSchema):
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


class PaymentModeRouteDetails(BaseSchema):
    pass


class StoredPaymentDetails(BaseSchema):
    pass


class WalletLinkRequestSchema(BaseSchema):
    pass


class WalletVerifyRequestSchema(BaseSchema):
    pass


class WalletDelinkRequestSchema(BaseSchema):
    pass


class WalletResponseSchema(BaseSchema):
    pass


class ResendOrCancelPayment(BaseSchema):
    pass


class LinkStatus(BaseSchema):
    pass


class ResendOrCancelPaymentDetails(BaseSchema):
    pass


class RenderHTML(BaseSchema):
    pass


class RenderHTMLDetails(BaseSchema):
    pass


class ValidateVPA(BaseSchema):
    pass


class ValidateUPI(BaseSchema):
    pass


class ValidateVPADetails(BaseSchema):
    pass


class CardDetails(BaseSchema):
    pass


class CardDetailsFetchedDetails(BaseSchema):
    pass


class TransferItemsDetails(BaseSchema):
    pass


class TransferModeDetails(BaseSchema):
    pass


class TransferModeFetchDetails(BaseSchema):
    pass


class UpdateRefundTransferMode(BaseSchema):
    pass


class RefundTransferModeUpdateDetails(BaseSchema):
    pass


class OrderBeneficiaryDetails(BaseSchema):
    pass


class OrderBeneficiaryFetchDetails(BaseSchema):
    pass


class NotFoundResourceError(BaseSchema):
    pass


class IfscCodeDetails(BaseSchema):
    pass


class ErrorCodeDescription(BaseSchema):
    pass


class AddBeneficiaryViaOtpVerification(BaseSchema):
    pass


class AddBeneficiaryViaOtpVerificationDetails(BaseSchema):
    pass


class WrongOtpError(BaseSchema):
    pass


class BeneficiaryModeDetails(BaseSchema):
    pass


class AddBeneficiaryDetails(BaseSchema):
    pass


class RefundAccountDetails(BaseSchema):
    pass


class BankDetailsForOTP(BaseSchema):
    pass


class AddBeneficiaryDetailsOTP(BaseSchema):
    pass


class WalletOtp(BaseSchema):
    pass


class WalletOtpDetails(BaseSchema):
    pass


class SetDefaultBeneficiary(BaseSchema):
    pass


class SetDefaultBeneficiaryDetails(BaseSchema):
    pass


class GetPaymentLinkDetails(BaseSchema):
    pass


class ErrorDescription(BaseSchema):
    pass


class ErrorDetails(BaseSchema):
    pass


class CreatePaymentLinkMeta(BaseSchema):
    pass


class CreatePaymentLink(BaseSchema):
    pass


class CreatePaymentLinkDetails(BaseSchema):
    pass


class CancelOrResendPaymentLink(BaseSchema):
    pass


class ResendPaymentLinkDetails(BaseSchema):
    pass


class CancelPaymentLinkDetails(BaseSchema):
    pass


class PollingPaymentLinkDetails(BaseSchema):
    pass


class PaymentMethodsMeta(BaseSchema):
    pass


class CreateOrderUserPaymentMethods(BaseSchema):
    pass


class CreateOrderUser(BaseSchema):
    pass


class CreateOrderUserData(BaseSchema):
    pass


class CreateOrderUserDetails(BaseSchema):
    pass


class BalanceDetails(BaseSchema):
    pass


class CreditSummary(BaseSchema):
    pass


class CustomerCreditSummaryDetails(BaseSchema):
    pass


class RedirectURL(BaseSchema):
    pass


class RedirectToAggregatorDetails(BaseSchema):
    pass


class CreditDetail(BaseSchema):
    pass


class CheckCreditDetails(BaseSchema):
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


class CustomerOnboarding(BaseSchema):
    pass


class OnboardSummary(BaseSchema):
    pass


class CustomerOnboardingDetails(BaseSchema):
    pass


class PaidOrderDetails(BaseSchema):
    pass


class DeleteRefundAccountDetails(BaseSchema):
    pass


class RefundOptionsDetails(BaseSchema):
    pass


class RefundOptions(BaseSchema):
    pass


class OfflineRefundOptions(BaseSchema):
    pass


class RefundOptionDetails(BaseSchema):
    pass


class SelectedRefundOptionDetails(BaseSchema):
    pass


class WalletBeneficiaryDetails(BaseSchema):
    pass


class UpiBeneficiaryDetails(BaseSchema):
    pass


class BeneficiaryRefundOptions(BaseSchema):
    pass


class OrderBeneficiaryDetailsSchemaV2(BaseSchema):
    pass


class ValidateValidateAddress(BaseSchema):
    pass


class VPADetails(BaseSchema):
    pass


class ValidateValidateAddressDetails(BaseSchema):
    pass


class PaymentMethodsMetaOrder(BaseSchema):
    pass


class PaymentOrderMethods(BaseSchema):
    pass


class PaymentOrder(BaseSchema):
    pass


class PaymentOrderData(BaseSchema):
    pass


class PaymentOrderDetails(BaseSchema):
    pass


class ShipmentRefund(BaseSchema):
    pass


class ShipmentRefundDetail(BaseSchema):
    pass


class ShipmentRefundDetails(BaseSchema):
    pass


class CustomerValidationSchema(BaseSchema):
    pass


class UserCreditSchema(BaseSchema):
    pass


class CreditAccountSummary(BaseSchema):
    pass


class ValidateCustomerCreditSchema(BaseSchema):
    pass


class RefundBeneficiaries(BaseSchema):
    pass


class UPIBeneficiary(BaseSchema):
    pass


class BankBeneficiary(BaseSchema):
    pass


class BeneficiaryDetails(BaseSchema):
    pass


class AddBeneficiaryRequestDetails(BaseSchema):
    pass


class AddBeneficiaryResponseDetails(BaseSchema):
    pass


class DeleteBeneficiary(BaseSchema):
    pass


class DeleteBeneficiaryDetails(BaseSchema):
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
    


class AggregatorsConfigDetail(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    razorpay = fields.Nested(AggregatorConfigDetail, required=False)
    
    juspay = fields.Nested(AggregatorConfigDetail, required=False)
    
    simpl = fields.Nested(AggregatorConfigDetail, required=False)
    
    payumoney = fields.Nested(AggregatorConfigDetail, required=False)
    
    ccavenue = fields.Nested(AggregatorConfigDetail, required=False)
    
    env = fields.Str(required=False)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class HttpErrorCodeAndResponseSchema(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    


class HttpErrorCodeDetails(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    


class AttachCard(BaseSchema):
    # Payment swagger.json

    
    nickname = fields.Str(required=False)
    
    refresh = fields.Boolean(required=False, allow_none=True)
    
    card_id = fields.Str(required=False)
    
    name_on_card = fields.Str(required=False)
    


class AttachCardsDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CardPaymentGateway(BaseSchema):
    # Payment swagger.json

    
    api = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False, allow_none=True)
    


class ActiveCardPaymentGatewayDetails(BaseSchema):
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
    


class ListCardsDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class DeleteCard(BaseSchema):
    # Payment swagger.json

    
    card_id = fields.Str(required=False)
    


class DeleteCardsDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class ValidateCustomer(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    phone_number = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    order_items = fields.List(fields.Dict(required=False), required=False)
    
    payload = fields.Str(required=False, allow_none=True)
    
    merchant_params = fields.Dict(required=False)
    
    delivery_address = fields.Dict(required=False)
    


class ValidateCustomerDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ChargeCustomer(BaseSchema):
    # Payment swagger.json

    
    verified = fields.Boolean(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    transaction_token = fields.Str(required=False, allow_none=True)
    
    amount = fields.Int(required=False)
    


class ChargeCustomerDetails(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    cart_id = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    delivery_address_id = fields.Str(required=False, allow_none=True)
    


class PaymentInitialization(BaseSchema):
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
    
    amount = fields.Int(required=False)
    
    email = fields.Str(required=False)
    


class PaymentInitializationDetails(BaseSchema):
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
    
    status_code = fields.Str(required=False, allow_none=True)
    


class PaymentStatusUpdate(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    virtual_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    amount = fields.Int(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    merchant_url = fields.Str(required=False)
    


class PaymentStatusUpdateDetails(BaseSchema):
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
    
    partial_payment_allowed = fields.Boolean(required=False)
    


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
    
    supported_methods = fields.List(fields.Nested(SupportedMethodDetails, required=False), required=False)
    
    stored_payment_details = fields.List(fields.Nested(StoredPaymentDetails, required=False), required=False)
    
    suggested_list = fields.List(fields.Str(required=False), required=False)
    
    flow = fields.Str(required=False)
    


class SupportedMethodDetails(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class AggregatorRoute(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False, allow_none=True)
    
    payment_flow_data = fields.Dict(required=False, allow_none=True)
    
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
    
    razorpay = fields.Nested(AggregatorRoute, required=False)
    
    juspay = fields.Nested(AggregatorRoute, required=False)
    
    simpl = fields.Nested(AggregatorRoute, required=False)
    
    ccavenue = fields.Nested(AggregatorRoute, required=False)
    
    payubiz = fields.Nested(AggregatorRoute, required=False)
    
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
    


class PaymentModeRouteDetails(BaseSchema):
    # Payment swagger.json

    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    
    success = fields.Boolean(required=False)
    
    payment_breakup = fields.Dict(required=False)
    
    advance_payment = fields.List(fields.Nested(AdvancePaymentObject, required=False), required=False)
    


class StoredPaymentDetails(BaseSchema):
    # Payment swagger.json

    
    aggregator_name = fields.Str(required=False)
    
    card_number = fields.Str(required=False, allow_none=True)
    
    card_reference = fields.Str(required=False, allow_none=True)
    
    card_issuer = fields.Str(required=False, allow_none=True)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False, allow_none=True)
    
    card_fingerprint = fields.Str(required=False, allow_none=True)
    
    expired = fields.Boolean(required=False, allow_none=True)
    
    exp_year = fields.Int(required=False, allow_none=True)
    
    exp_month = fields.Int(required=False, allow_none=True)
    
    card_id = fields.Str(required=False, allow_none=True)
    
    card_brand = fields.Str(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    nickname = fields.Str(required=False, allow_none=True)
    
    card_name = fields.Str(required=False, allow_none=True)
    
    card_type = fields.Str(required=False, allow_none=True)
    
    card_brand_image = fields.Str(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    card_isin = fields.Str(required=False, allow_none=True)
    
    cvv_length = fields.Int(required=False, allow_none=True)
    
    cvv_less = fields.Boolean(required=False, allow_none=True)
    
    card_token = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    vpa = fields.Str(required=False, allow_none=True)
    


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
    


class ResendOrCancelPayment(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    request_type = fields.Str(required=False)
    


class LinkStatus(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    is_payment_done = fields.Boolean(required=False)
    


class ResendOrCancelPaymentDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(LinkStatus, required=False)
    
    success = fields.Boolean(required=False)
    


class RenderHTML(BaseSchema):
    # Payment swagger.json

    
    returntype = fields.Str(required=False, allow_none=True)
    
    base64_html = fields.Str(required=False)
    


class RenderHTMLDetails(BaseSchema):
    # Payment swagger.json

    
    html = fields.Str(required=False)
    


class ValidateVPA(BaseSchema):
    # Payment swagger.json

    
    upi_vpa = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    


class ValidateUPI(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    upi_vpa = fields.Str(required=False)
    


class ValidateVPADetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ValidateUPI, required=False)
    
    success = fields.Boolean(required=False)
    


class CardDetails(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    country = fields.Str(required=False)
    
    bank_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    card_exp_year = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    card_sub_type = fields.Str(required=False)
    
    is_domestic_card = fields.Boolean(required=False)
    
    name_on_card = fields.Str(required=False)
    
    card_exp_month = fields.Str(required=False)
    
    extended_card_type = fields.Str(required=False)
    
    card_object = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    bank = fields.Str(required=False)
    
    cvv_length = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    is_enabled = fields.Boolean(required=False)
    
    is_card_valid = fields.Boolean(required=False)
    


class CardDetailsFetchedDetails(BaseSchema):
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
    


class TransferModeFetchDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(TransferModeDetails, required=False), required=False)
    


class UpdateRefundTransferMode(BaseSchema):
    # Payment swagger.json

    
    enable = fields.Boolean(required=False)
    
    transfer_mode = fields.Str(required=False)
    


class RefundTransferModeUpdateDetails(BaseSchema):
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
    


class OrderBeneficiaryFetchDetails(BaseSchema):
    # Payment swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    


class NotFoundResourceError(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class IfscCodeDetails(BaseSchema):
    # Payment swagger.json

    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    bank_name = fields.Str(required=False)
    


class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class AddBeneficiaryViaOtpVerification(BaseSchema):
    # Payment swagger.json

    
    request_id = fields.Str(required=False)
    
    hash_key = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class AddBeneficiaryViaOtpVerificationDetails(BaseSchema):
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
    


class AddBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    delights = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    
    otp = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    


class RefundAccountDetails(BaseSchema):
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
    


class AddBeneficiaryDetailsOTP(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    


class WalletOtp(BaseSchema):
    # Payment swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class WalletOtpDetails(BaseSchema):
    # Payment swagger.json

    
    request_id = fields.Str(required=False)
    
    is_verified_flag = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class SetDefaultBeneficiary(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    


class SetDefaultBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    is_beneficiary_set = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class GetPaymentLinkDetails(BaseSchema):
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
    


class ErrorDetails(BaseSchema):
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
    


class CreatePaymentLink(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False, allow_none=True)
    
    external_order_id = fields.Str(required=False)
    
    mobile_number = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    email = fields.Str(required=False)
    
    success_redirection_url = fields.Str(required=False)
    
    failure_redirection_url = fields.Str(required=False)
    
    send_communication = fields.Boolean(required=False)
    


class CreatePaymentLinkDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    payment_link_url = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False, allow_none=True)
    


class CancelOrResendPaymentLink(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    


class ResendPaymentLinkDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CancelPaymentLinkDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class PollingPaymentLinkDetails(BaseSchema):
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
    


class CreateOrderUser(BaseSchema):
    # Payment swagger.json

    
    currency = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    payment_methods = fields.Nested(CreateOrderUserPaymentMethods, required=False)
    
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
    


class CreateOrderUserDetails(BaseSchema):
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
    


class CustomerCreditSummaryDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(CreditSummary, required=False)
    
    success = fields.Boolean(required=False)
    


class RedirectURL(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    redirect_url = fields.Str(required=False)
    
    extra = fields.Str(required=False)
    


class RedirectToAggregatorDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(RedirectURL, required=False)
    
    success = fields.Boolean(required=False)
    


class CreditDetail(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    is_registered = fields.Boolean(required=False)
    
    signup_url = fields.Str(required=False)
    
    available_credit = fields.Float(required=False)
    


class CheckCreditDetails(BaseSchema):
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
    
    dob = fields.Str(required=False)
    
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
    


class CustomerOnboarding(BaseSchema):
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
    


class CustomerOnboardingDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(OnboardSummary, required=False)
    
    success = fields.Boolean(required=False)
    


class PaidOrderDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class DeleteRefundAccountDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


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
    


class RefundOptionDetails(BaseSchema):
    # Payment swagger.json

    
    offline_refund_options = fields.Nested(OfflineRefundOptions, required=False)
    
    success = fields.Boolean(required=False)
    
    refund_options = fields.Nested(RefundOptions, required=False)
    


class SelectedRefundOptionDetails(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Dict(required=False)
    
    shipment_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
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
    


class OrderBeneficiaryDetailsSchemaV2(BaseSchema):
    # Payment swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    data = fields.Nested(BeneficiaryRefundOptions, required=False)
    
    limit = fields.Dict(required=False)
    


class ValidateValidateAddress(BaseSchema):
    # Payment swagger.json

    
    ifsc_code = fields.Str(required=False)
    
    upi_vpa = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False, allow_none=True)
    


class VPADetails(BaseSchema):
    # Payment swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    upi_vpa = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    


class ValidateValidateAddressDetails(BaseSchema):
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
    


class PaymentOrder(BaseSchema):
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
    


class PaymentOrderDetails(BaseSchema):
    # Payment swagger.json

    
    payment_confirm_url = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    data = fields.Nested(PaymentOrderData, required=False)
    
    message = fields.Str(required=False)
    


class ShipmentRefund(BaseSchema):
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
    


class ShipmentRefundDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ShipmentRefundDetail, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CustomerValidationSchema(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    transaction_amount = fields.Float(required=False)
    
    cart_id = fields.Str(required=False)
    


class UserCreditSchema(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    


class CreditAccountSummary(BaseSchema):
    # Payment swagger.json

    
    account_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    redeemable_balance = fields.Nested(UserCreditSchema, required=False)
    
    available_balance = fields.Nested(UserCreditSchema, required=False)
    
    amount_on_hold = fields.List(fields.Nested(UserCreditSchema, required=False), required=False)
    


class ValidateCustomerCreditSchema(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    is_eligible = fields.Boolean(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    account = fields.Nested(CreditAccountSummary, required=False)
    


class RefundBeneficiaries(BaseSchema):
    # Payment swagger.json

    
    upi = fields.List(fields.Nested(UPIBeneficiary, required=False), required=False)
    
    bank = fields.List(fields.Nested(BankBeneficiary, required=False), required=False)
    


class UPIBeneficiary(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    is_verified = fields.Boolean(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    vpa_address = fields.Str(required=False)
    
    customer_name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class BankBeneficiary(BaseSchema):
    # Payment swagger.json

    
    ifsc_code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_verified = fields.Boolean(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class BeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    account_holder = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    upi = fields.Str(required=False)
    


class AddBeneficiaryRequestDetails(BaseSchema):
    # Payment swagger.json

    
    details = fields.Nested(BeneficiaryDetails, required=False)
    
    order_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    


class AddBeneficiaryResponseDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    is_verified = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    upi = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class DeleteBeneficiary(BaseSchema):
    # Payment swagger.json

    
    beneficiary_id = fields.Str(required=False)
    


class DeleteBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    


