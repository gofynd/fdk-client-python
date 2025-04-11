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


class HttpErrorCodeDetails(BaseSchema):
    pass


class PaymentErrorCodeAndMessage(BaseSchema):
    pass


class PaymentOptionErrorDetails(BaseSchema):
    pass


class PaymentPOSOptionErrorDetails(BaseSchema):
    pass


class OrderErrorDetails(BaseSchema):
    pass


class PaymentError(BaseSchema):
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


class ValidateCustomerInfo(BaseSchema):
    pass


class ValidateCustomerData(BaseSchema):
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


class ProductCODData(BaseSchema):
    pass


class CODChargesLimitsDetails(BaseSchema):
    pass


class PaymentModeList(BaseSchema):
    pass


class RootPaymentMode(BaseSchema):
    pass


class PaymentConfig(BaseSchema):
    pass


class GatewayData(BaseSchema):
    pass


class SDKDetails(BaseSchema):
    pass


class SDKConfig(BaseSchema):
    pass


class UserData(BaseSchema):
    pass


class PaymentFlowData(BaseSchema):
    pass


class AggregatorRouteData(BaseSchema):
    pass


class AggregatorRoute(BaseSchema):
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


class WalletLinkRequestSchema(BaseSchema):
    pass


class WalletVerifyRequestSchema(BaseSchema):
    pass


class WalletDelinkRequestSchema(BaseSchema):
    pass


class WalletResponseSchema(BaseSchema):
    pass


class WalletResponseData(BaseSchema):
    pass


class RupifiBannerData(BaseSchema):
    pass


class RupifiBannerDetails(BaseSchema):
    pass


class EpaylaterBannerData(BaseSchema):
    pass


class EpaylaterBannerDetails(BaseSchema):
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


class RefundData(BaseSchema):
    pass


class AddBeneficiaryDetailsOTPDetails(BaseSchema):
    pass


class PostAddBeneficiaryDetailsOTPDetails(BaseSchema):
    pass


class PostBankDetailsForOTP(BaseSchema):
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


class RefundOrderBen(BaseSchema):
    pass


class RefundOrderBenDetails(BaseSchema):
    pass


class GetPaymentLinkDetails(BaseSchema):
    pass


class ErrorDescription(BaseSchema):
    pass


class ErrorDetails(BaseSchema):
    pass


class PollingPaymentLinkError(BaseSchema):
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


class PaymentLinkError(BaseSchema):
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


class OutstandingOrderDetails(BaseSchema):
    pass


class PaidOrderDetails(BaseSchema):
    pass


class DeleteBeneficiary(BaseSchema):
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


class RefundOptionsLimit(BaseSchema):
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


class CustomerDetails(BaseSchema):
    pass


class PaymentOrderData(BaseSchema):
    pass


class PaymentOrderDetails(BaseSchema):
    pass


class ShipmentRefundRequestMeta(BaseSchema):
    pass


class ShipmentRefund(BaseSchema):
    pass


class ShipmentRefundDetail(BaseSchema):
    pass


class ShipmentRefundDetails(BaseSchema):
    pass


class RefundOptionsPriority(BaseSchema):
    pass


class RefundItem(BaseSchema):
    pass


class Version(BaseSchema):
    pass


class VersionDetails(BaseSchema):
    pass


class RefundErrorCodeAndMessage(BaseSchema):
    pass


class IFSCErrorData(BaseSchema):
    pass


class EDCError(BaseSchema):
    pass


class RefundOptionErrorCodeAndMessage(BaseSchema):
    pass


class RefundOptionMessage(BaseSchema):
    pass


class RefundOptionError(BaseSchema):
    pass


class CardData(BaseSchema):
    pass


class Account(BaseSchema):
    pass


class CartData(BaseSchema):
    pass


class Article(BaseSchema):
    pass


class Weight(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class Manufacturer(BaseSchema):
    pass


class ArticleAssignment(BaseSchema):
    pass


class CartUser(BaseSchema):
    pass


class Affiliate(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class PaymentMethod(BaseSchema):
    pass


class CardReq(BaseSchema):
    pass


class UpdateAggregatorCardReq(BaseSchema):
    pass


class UpdateAggregatorCardDetails(BaseSchema):
    pass


class AggregatorCard(BaseSchema):
    pass


class UpdateCard(BaseSchema):
    pass


class PaymentCallbackDetails(BaseSchema):
    pass


class PaymentConfirmation(BaseSchema):
    pass


class MultiTenderPaymentMethod(BaseSchema):
    pass


class MultiTenderPaymentMeta(BaseSchema):
    pass


class PaymentConfirmationDetails(BaseSchema):
    pass


class HttpErrorCodeAndMessage(BaseSchema):
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
    
    merchant_id = fields.Raw(required=False)
    
    api_domain = fields.Str(required=False, allow_none=True)
    
    webhook_username = fields.Str(required=False)
    
    webhook_password = fields.Str(required=False)
    
    signature_key = fields.Str(required=False)
    
    merchant_salt = fields.Str(required=False)
    
    checkout_formpost_url = fields.Str(required=False)
    
    refund_api_domain = fields.Str(required=False)
    
    non_trxn_url = fields.Str(required=False)
    
    trxn_url = fields.Str(required=False)
    
    webhook_secret = fields.Str(required=False)
    
    is_sub_fynd_account = fields.Str(required=False, allow_none=True)
    
    vpa = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    secret_key = fields.Str(required=False)
    
    product_id = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    is_active = fields.Raw(required=False)
    


class AggregatorsConfigDetail(BaseSchema):
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
    
    ajiodhan = fields.Nested(AggregatorConfigDetail, required=False)
    
    potlee = fields.Nested(AggregatorConfigDetail, required=False)
    
    qr_refund_jiopay = fields.Nested(AggregatorConfigDetail, required=False)
    
    offerxone = fields.Nested(AggregatorConfigDetail, required=False)
    
    env = fields.Str(required=False)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class HttpErrorCodeDetails(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentErrorCodeAndMessage(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(PaymentError, required=False)
    
    success = fields.Boolean(required=False)
    
    error_msg = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class PaymentOptionErrorDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentPOSOptionErrorDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Nested(PaymentError, required=False)
    
    success = fields.Boolean(required=False)
    


class OrderErrorDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ErrorDetails, required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentError(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.List(fields.Str(required=False), required=False)
    
    transaction_amount_in_paise = fields.List(fields.Str(required=False), required=False)
    


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
    
    status = fields.Int(required=False)
    


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

    
    success = fields.Boolean(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    status = fields.Int(required=False)
    


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

    
    data = fields.Nested(ValidateCustomerInfo, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Nested(ValidateCustomerInfo, required=False)
    


class ValidateCustomerInfo(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ValidateCustomerData, required=False)
    
    aggregator = fields.Str(required=False)
    
    api_version = fields.Int(required=False)
    


class ValidateCustomerData(BaseSchema):
    # Payment swagger.json

    
    approved = fields.Boolean(required=False)
    
    button_text = fields.Str(required=False)
    
    first_transaction = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
    customer_mobile_number = fields.Str(required=False)
    
    total_credited_balance = fields.Float(required=False)
    
    is_cn_locked = fields.Boolean(required=False)
    
    total_locked_amount = fields.Float(required=False)
    
    allowed_redemption_amount = fields.Float(required=False)
    


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
    
    cart_id = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
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
    
    merchant_transaction_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    amount = fields.Int(required=False)
    
    email = fields.Str(required=False)
    
    unique_link_id = fields.Str(required=False)
    


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
    
    merchant_transaction_id = fields.Str(required=False)
    
    customer_id = fields.Str(required=False, allow_none=True)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    currency = fields.Str(required=False, allow_none=True)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    amount = fields.Int(required=False, allow_none=True)
    
    bqr_image = fields.Str(required=False, allow_none=True)
    
    unique_link_id = fields.Str(required=False)
    
    status_code = fields.Str(required=False, allow_none=True)
    


class PaymentStatusUpdate(BaseSchema):
    # Payment swagger.json

    
    aggregator_order_id = fields.Str(required=False)
    
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
    
    amount = fields.Int(required=False)
    
    email = fields.Str(required=False)
    
    unique_link_id = fields.Str(required=False)
    
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
    


class ProductCODData(BaseSchema):
    # Payment swagger.json

    
    items = fields.Dict(required=False, allow_none=True)
    
    cod_charges = fields.Nested(CODChargesLimitsDetails, required=False)
    


class CODChargesLimitsDetails(BaseSchema):
    # Payment swagger.json

    
    max_cart_value = fields.Float(required=False, allow_none=True)
    
    min_cart_value = fields.Float(required=False, allow_none=True)
    
    cod_charge = fields.Float(required=False, allow_none=True)
    


class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    meta = fields.Dict(required=False, allow_none=True)
    
    collect_flow = fields.Boolean(required=False)
    
    provider = fields.Str(required=False, allow_none=True)
    
    wallet_name = fields.Str(required=False, allow_none=True)
    
    wallet_code = fields.Str(required=False, allow_none=True)
    
    wallet_id = fields.Int(required=False, allow_none=True)
    
    bank_name = fields.Str(required=False, allow_none=True)
    
    bank_code = fields.Str(required=False, allow_none=True)
    
    url = fields.Str(required=False, allow_none=True)
    
    remaining_limit = fields.Float(required=False, allow_none=True)
    
    card_brand = fields.Str(required=False, allow_none=True)
    
    card_fingerprint = fields.Str(required=False, allow_none=True)
    
    merchant_code = fields.Str(required=False, allow_none=True)
    
    intent_flow = fields.Boolean(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    card_issuer = fields.Str(required=False, allow_none=True)
    
    cod_limit_per_order = fields.Float(required=False, allow_none=True)
    
    card_reference = fields.Str(required=False, allow_none=True)
    
    card_type = fields.Str(required=False, allow_none=True)
    
    card_isin = fields.Str(required=False, allow_none=True)
    
    exp_month = fields.Int(required=False, allow_none=True)
    
    fynd_vpa = fields.Str(required=False, allow_none=True)
    
    card_number = fields.Str(required=False, allow_none=True)
    
    display_priority = fields.Int(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    card_id = fields.Str(required=False, allow_none=True)
    
    retry_count = fields.Int(required=False, allow_none=True)
    
    card_name = fields.Str(required=False, allow_none=True)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    intent_app_error_dict_list = fields.List(fields.Nested(IntentAppErrorList, required=False), required=False)
    
    card_brand_image = fields.Str(required=False, allow_none=True)
    
    expired = fields.Boolean(required=False, allow_none=True)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    card_token = fields.Str(required=False, allow_none=True)
    
    aggregator_name = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False, allow_none=True)
    
    product_cod_data = fields.Nested(ProductCODData, required=False)
    
    cod_limit = fields.Float(required=False, allow_none=True)
    
    intent_app = fields.List(fields.Nested(IntentApp, required=False), required=False)
    
    nickname = fields.Str(required=False, allow_none=True)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False, allow_none=True)
    
    exp_year = fields.Int(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    


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
    
    payment_mode_id = fields.Int(required=False, allow_none=True)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    version = fields.Nested(Version, required=False)
    


class PaymentConfig(BaseSchema):
    # Payment swagger.json

    
    redirect = fields.Boolean(required=False, allow_none=True)
    
    final_payment_action_url = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    action_url = fields.Str(required=False, allow_none=True)
    


class GatewayData(BaseSchema):
    # Payment swagger.json

    
    route = fields.Str(required=False, allow_none=True)
    
    entity = fields.Str(required=False, allow_none=True)
    
    is_customer_validation_required = fields.Boolean(required=False, allow_none=True)
    
    cust_validation_url = fields.Str(required=False, allow_none=True)
    
    sdk = fields.Nested(SDKDetails, required=False)
    
    return_url = fields.Str(required=False, allow_none=True)
    
    user_email = fields.Str(required=False, allow_none=True)
    
    user_phone = fields.Str(required=False, allow_none=True)
    


class SDKDetails(BaseSchema):
    # Payment swagger.json

    
    config = fields.Nested(SDKConfig, required=False)
    
    data = fields.Nested(UserData, required=False)
    


class SDKConfig(BaseSchema):
    # Payment swagger.json

    
    redirect = fields.Boolean(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    action_url = fields.Str(required=False, allow_none=True)
    


class UserData(BaseSchema):
    # Payment swagger.json

    
    user_phone = fields.Str(required=False, allow_none=True)
    
    user_email = fields.Str(required=False, allow_none=True)
    


class PaymentFlowData(BaseSchema):
    # Payment swagger.json

    
    is_customer_validation_required = fields.Boolean(required=False)
    
    cust_validation_url = fields.Str(required=False, allow_none=True)
    
    config = fields.Nested(PaymentConfig, required=False)
    
    data = fields.Nested(GatewayData, required=False)
    
    return_url = fields.Str(required=False, allow_none=True)
    


class AggregatorRouteData(BaseSchema):
    # Payment swagger.json

    
    gateway = fields.Nested(GatewayData, required=False)
    
    payment_flow_data = fields.Nested(PaymentFlowData, required=False)
    
    data = fields.Nested(GatewayData, required=False)
    
    payment_flow = fields.Str(required=False, allow_none=True)
    
    api_link = fields.Str(required=False, allow_none=True)
    
    route = fields.Str(required=False, allow_none=True)
    
    entity = fields.Str(required=False, allow_none=True)
    
    is_customer_validation_required = fields.Boolean(required=False)
    
    cust_validation_url = fields.Str(required=False, allow_none=True)
    
    sdk = fields.Nested(SDKDetails, required=False)
    
    return_url = fields.Str(required=False, allow_none=True)
    
    user_email = fields.Str(required=False, allow_none=True)
    
    user_phone = fields.Str(required=False, allow_none=True)
    


class AggregatorRoute(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(AggregatorRouteData, required=False)
    
    payment_flow_data = fields.Dict(required=False, allow_none=True)
    
    payment_flow = fields.Str(required=False, allow_none=True)
    
    api_link = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False, allow_none=True)
    


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
    
    jio = fields.Nested(AggregatorRoute, required=False)
    
    payumoney = fields.Nested(AggregatorRoute, required=False)
    
    openapi = fields.Nested(AggregatorRoute, required=False)
    
    potlee = fields.Nested(AggregatorRoute, required=False)
    
    upi_razorpay = fields.Nested(AggregatorRoute, required=False)
    
    creditnote = fields.Nested(AggregatorRoute, required=False)
    
    pinelabs = fields.Nested(AggregatorRoute, required=False)
    
    checkout = fields.Nested(AggregatorRoute, required=False)
    
    cashfree = fields.Nested(AggregatorRoute, required=False)
    
    jio_extension = fields.Nested(AggregatorRoute, required=False)
    
    offerxone = fields.Nested(AggregatorRoute, required=False)
    


class PaymentOptionAndFlow(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    


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
    
    all_cancellation_type = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
    allow_custom_advance_amount = fields.Boolean(required=False, allow_none=True)
    


class SplitObject(BaseSchema):
    # Payment swagger.json

    
    total_number_of_splits = fields.Float(required=False, allow_none=True)
    
    splits_remaining = fields.Float(required=False, allow_none=True)
    
    amount_remaining = fields.Float(required=False, allow_none=True)
    


class AdvancePaymentObject(BaseSchema):
    # Payment swagger.json

    
    version = fields.Nested(Version, required=False)
    
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
    
    wallet_id = fields.Str(required=False)
    


class WalletResponseSchema(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(WalletResponseData, required=False)
    
    success = fields.Boolean(required=False)
    


class WalletResponseData(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    link_token = fields.Str(required=False)
    


class RupifiBannerData(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    kyc_url = fields.Str(required=False)
    


class RupifiBannerDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(RupifiBannerData, required=False)
    
    success = fields.Boolean(required=False)
    


class EpaylaterBannerData(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    display = fields.Boolean(required=False)
    


class EpaylaterBannerDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EpaylaterBannerData, required=False)
    
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

    
    status = fields.Boolean(required=False)
    
    customer_name = fields.Str(required=False, allow_none=True)
    
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
    
    aggregator_id = fields.Str(required=False, allow_none=True)
    
    is_verified = fields.Boolean(required=False, allow_none=True)
    
    status = fields.Str(required=False, allow_none=True)
    
    txn_id = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    default_beneficiary = fields.Boolean(required=False, allow_none=True)
    


class OrderBeneficiaryFetchDetails(BaseSchema):
    # Payment swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    
    bank = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    


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
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class BeneficiaryModeDetails(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    email = fields.Str(required=False, allow_none=True)
    
    vpa = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    wallet = fields.Str(required=False, allow_none=True)
    
    beneficiary_id = fields.Str(required=False)
    


class AddBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    delights = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    


class RefundAccountDetails(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    data = fields.Nested(RefundData, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class RefundData(BaseSchema):
    # Payment swagger.json

    
    bene_name_mismatch = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    subcode = fields.Str(required=False, allow_none=True)
    
    hash_key = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    request_id = fields.Int(required=False, allow_none=True)
    
    beneficiary_id = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    


class AddBeneficiaryDetailsOTPDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(BankDetailsForOTP, required=False), required=False)
    
    message = fields.Str(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    


class PostAddBeneficiaryDetailsOTPDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(PostBankDetailsForOTP, required=False)
    
    message = fields.Str(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    


class PostBankDetailsForOTP(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class BankDetailsForOTP(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    


class AddBeneficiaryDetailsOTP(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    request_hash = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    


class WalletOtp(BaseSchema):
    # Payment swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class WalletOtpDetails(BaseSchema):
    # Payment swagger.json

    
    request_id = fields.Str(required=False, allow_none=True)
    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class SetDefaultBeneficiary(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    merchant_shipment_id = fields.Str(required=False)
    


class SetDefaultBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    is_beneficiary_set = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class RefundOrderBen(BaseSchema):
    # Payment swagger.json

    
    order_ids = fields.List(fields.Str(required=False), required=False)
    


class RefundOrderBenDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False, allow_none=True)
    


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
    
    currency = fields.Str(required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    


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
    
    description = fields.Str(required=False, allow_none=True)
    


class ErrorDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PollingPaymentLinkError(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CreatePaymentLinkMeta(BaseSchema):
    # Payment swagger.json

    
    cart_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    assign_card_id = fields.Str(required=False, allow_none=True)
    
    amount = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class CreatePaymentLink(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False, allow_none=True)
    
    external_order_id = fields.Str(required=False)
    
    mobile_number = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    email = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    success_redirection_url = fields.Str(required=False)
    
    failure_redirection_url = fields.Str(required=False)
    


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
    
    error = fields.Nested(PaymentLinkError, required=False)
    


class PaymentLinkError(BaseSchema):
    # Payment swagger.json

    
    cancelled = fields.Boolean(required=False)
    
    msg = fields.Str(required=False)
    


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
    
    failure_callback_url = fields.Str(required=False)
    
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
    
    base64_html = fields.Str(required=False, allow_none=True)
    


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
    
    message = fields.Str(required=False)
    


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
    
    state = fields.Str(required=False)
    


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
    
    type = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class CustomerOnboardingDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(OnboardSummary, required=False)
    
    success = fields.Boolean(required=False)
    


class OutstandingOrderDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class PaidOrderDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class DeleteBeneficiary(BaseSchema):
    # Payment swagger.json

    
    beneficiary_id = fields.Str(required=False)
    


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
    
    offline_refund_collect_type = fields.List(fields.Str(required=False), required=False)
    


class OfflineRefundOptions(BaseSchema):
    # Payment swagger.json

    
    items = fields.Nested(RefundOptionsDetails, required=False)
    
    payment_modes = fields.List(fields.Str(required=False), required=False)
    
    offline_refund_collect_type = fields.List(fields.Str(required=False), required=False)
    


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
    
    beneficiary_details = fields.Dict(required=False)
    


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

    
    bank = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    wallet = fields.Nested(WalletBeneficiaryDetails, required=False)
    
    upi = fields.Nested(UpiBeneficiaryDetails, required=False)
    


class OrderBeneficiaryDetailsSchemaV2(BaseSchema):
    # Payment swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    data = fields.Nested(BeneficiaryRefundOptions, required=False)
    
    limit = fields.Nested(RefundOptionsLimit, required=False)
    


class RefundOptionsLimit(BaseSchema):
    # Payment swagger.json

    
    bank = fields.Int(required=False)
    
    wallet = fields.Int(required=False)
    
    upi = fields.Int(required=False)
    


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
    
    vpa = fields.Nested(VPADetails, required=False)
    


class PaymentMethodsMetaOrder(BaseSchema):
    # Payment swagger.json

    
    merchant_code = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_extra_identifiers = fields.Dict(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    


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
    
    customer_details = fields.Nested(CustomerDetails, required=False)
    


class CustomerDetails(BaseSchema):
    # Payment swagger.json

    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


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
    
    bank = fields.Str(required=False, allow_none=True)
    
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
    


class ShipmentRefundRequestMeta(BaseSchema):
    # Payment swagger.json

    
    shipment_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    utr = fields.Str(required=False)
    
    notes = fields.Str(required=False, allow_none=True)
    
    billing_employee_code = fields.Str(required=False, allow_none=True)
    


class ShipmentRefund(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False, allow_none=True)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Nested(ShipmentRefundRequestMeta, required=False)
    


class ShipmentRefundDetail(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    


class ShipmentRefundDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ShipmentRefundDetail, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    refund_options = fields.Str(required=False)
    
    refund_options_priority = fields.Nested(RefundOptionsPriority, required=False)
    
    offline_refund_options_priority = fields.Nested(RefundOptionsPriority, required=False)
    


class RefundOptionsPriority(BaseSchema):
    # Payment swagger.json

    
    payment_modes = fields.List(fields.Str(required=False), required=False)
    
    items = fields.List(fields.Nested(RefundItem, required=False), required=False)
    
    payment_gateways = fields.List(fields.Str(required=False), required=False)
    
    offline_refund_collect_type = fields.List(fields.Str(required=False), required=False)
    


class RefundItem(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class Version(BaseSchema):
    # Payment swagger.json

    
    razorpay = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    rupifi = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    jio = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    stripe = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    payumoney = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    jiopay = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    fynd = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    potlee = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    juspay = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    simpl = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    
    checkout = fields.List(fields.Nested(VersionDetails, required=False), required=False)
    


class VersionDetails(BaseSchema):
    # Payment swagger.json

    
    version = fields.Str(required=False)
    


class RefundErrorCodeAndMessage(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(IFSCErrorData, required=False)
    
    error = fields.Nested(EDCError, required=False)
    
    errors = fields.Nested(EDCError, required=False)
    


class IFSCErrorData(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    subcode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class EDCError(BaseSchema):
    # Payment swagger.json

    
    error = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class RefundOptionErrorCodeAndMessage(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Nested(RefundOptionMessage, required=False)
    
    error = fields.Nested(RefundOptionError, required=False)
    


class RefundOptionMessage(BaseSchema):
    # Payment swagger.json

    
    code = fields.Int(required=False)
    
    description = fields.Nested(RefundOptionError, required=False)
    
    shipment_id = fields.List(fields.Str(required=False), required=False)
    
    order_id = fields.List(fields.Str(required=False), required=False)
    


class RefundOptionError(BaseSchema):
    # Payment swagger.json

    
    code = fields.Int(required=False)
    
    shipment_id = fields.List(fields.Str(required=False), required=False)
    
    order_id = fields.List(fields.Str(required=False), required=False)
    
    merchant_user_id = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Nested(lambda: RefundOptionError(exclude=('description')), required=False)
    


class CardData(BaseSchema):
    # Payment swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    number = fields.Str(required=False, allow_none=True)
    
    expiration_date = fields.Str(required=False, allow_none=True)
    


class Account(BaseSchema):
    # Payment swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    routing_number = fields.Str(required=False, allow_none=True)
    
    account_number = fields.Str(required=False, allow_none=True)
    


class CartData(BaseSchema):
    # Payment swagger.json

    
    _id = fields.Str(required=False, allow_none=True)
    
    uid = fields.Int(required=False, allow_none=True)
    
    gstin = fields.Str(required=False, allow_none=True)
    
    comment = fields.Str(required=False, allow_none=True)
    
    user_id = fields.Str(required=False, allow_none=True)
    
    articles = fields.List(fields.Nested(Article, required=False), required=False)
    
    cashback = fields.Int(required=False, allow_none=True)
    
    discount = fields.Int(required=False, allow_none=True)
    
    shipment = fields.Dict(required=False, allow_none=True)
    
    expire_at = fields.Str(required=False, allow_none=True)
    
    cart_value = fields.Int(required=False, allow_none=True)
    
    created_on = fields.Str(required=False, allow_none=True)
    
    is_archive = fields.Boolean(required=False, allow_none=True)
    
    is_default = fields.Boolean(required=False, allow_none=True)
    
    cod_charges = fields.Int(required=False, allow_none=True)
    
    coupon_code = fields.Str(required=False, allow_none=True)
    
    coupon_value = fields.Int(required=False, allow_none=True)
    
    fc_index_map = fields.List(fields.Int(required=False), required=False)
    
    fynd_credits = fields.Int(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False, allow_none=True)
    
    checkout_mode = fields.Str(required=False, allow_none=True)
    
    last_modified = fields.Str(required=False, allow_none=True)
    
    total_quantity = fields.Int(required=False, allow_none=True)
    
    cashback_applied = fields.Int(required=False, allow_none=True)
    
    delivery_charges = fields.Int(required=False, allow_none=True)
    
    applied_coupon_id = fields.Str(required=False, allow_none=True)
    
    original_cart_value = fields.Int(required=False, allow_none=True)
    
    bulk_coupon_discount = fields.Int(required=False, allow_none=True)
    
    fynd_credits_auto_applied = fields.Boolean(required=False, allow_none=True)
    


class Article(BaseSchema):
    # Payment swagger.json

    
    set = fields.Dict(required=False, allow_none=True)
    
    uid = fields.Str(required=False, allow_none=True)
    
    c_name = fields.Str(required=False, allow_none=True)
    
    is_set = fields.Boolean(required=False, allow_none=True)
    
    s_city = fields.Str(required=False, allow_none=True)
    
    weight = fields.Nested(Weight, required=False)
    
    avl_qty = fields.Int(required=False, allow_none=True)
    
    fragile = fields.Boolean(required=False, allow_none=True)
    
    item_id = fields.Int(required=False, allow_none=True)
    
    brand_id = fields.Int(required=False, allow_none=True)
    
    cashback = fields.Int(required=False, allow_none=True)
    
    discount = fields.Int(required=False, allow_none=True)
    
    hsn_code = fields.Str(required=False, allow_none=True)
    
    is_valid = fields.Boolean(required=False, allow_none=True)
    
    latitude = fields.Float(required=False, allow_none=True)
    
    quantity = fields.Int(required=False, allow_none=True)
    
    raw_meta = fields.Dict(required=False, allow_none=True)
    
    store_id = fields.Int(required=False, allow_none=True)
    
    dimension = fields.Nested(Dimension, required=False)
    
    item_size = fields.Str(required=False, allow_none=True)
    
    longitude = fields.Float(required=False, allow_none=True)
    
    old_price = fields.Int(required=False, allow_none=True)
    
    article_id = fields.Str(required=False, allow_none=True)
    
    company_id = fields.Int(required=False, allow_none=True)
    
    gst_amount = fields.Int(required=False, allow_none=True)
    
    identifier = fields.Dict(required=False, allow_none=True)
    
    store_name = fields.Str(required=False, allow_none=True)
    
    unit_price = fields.Int(required=False, allow_none=True)
    
    amount_paid = fields.Int(required=False, allow_none=True)
    
    bulk_margin = fields.Int(required=False, allow_none=True)
    
    cod_charges = fields.Int(required=False, allow_none=True)
    
    custom_meta = fields.Dict(required=False, allow_none=True)
    
    article_code = fields.Str(required=False, allow_none=True)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    price_marked = fields.Int(required=False, allow_none=True)
    
    bulk_discount = fields.Int(required=False, allow_none=True)
    
    store_pincode = fields.Int(required=False, allow_none=True)
    
    value_of_good = fields.Int(required=False, allow_none=True)
    
    last_update_at = fields.Str(required=False, allow_none=True)
    
    return_allowed = fields.Boolean(required=False, allow_none=True)
    
    transfer_price = fields.Int(required=False, allow_none=True)
    
    price_effective = fields.Int(required=False, allow_none=True)
    
    valid_inventory = fields.Boolean(required=False, allow_none=True)
    
    bulk_coupon_code = fields.Str(required=False, allow_none=True)
    
    cashback_applied = fields.Int(required=False, allow_none=True)
    
    delivery_charges = fields.Int(required=False, allow_none=True)
    
    mongo_article_id = fields.Str(required=False, allow_none=True)
    
    referral_credits = fields.Int(required=False, allow_none=True)
    
    country_of_origin = fields.Str(required=False, allow_none=True)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    gst_tax_percentage = fields.Int(required=False, allow_none=True)
    
    cancellation_allowed = fields.Boolean(required=False, allow_none=True)
    
    coupon_article_count = fields.Int(required=False, allow_none=True)
    
    size_level_total_qty = fields.Int(required=False, allow_none=True)
    
    article_assign_status = fields.Boolean(required=False, allow_none=True)
    
    quantity_assign_status = fields.Boolean(required=False, allow_none=True)
    
    coupon_effective_discount = fields.Int(required=False, allow_none=True)
    


class Weight(BaseSchema):
    # Payment swagger.json

    
    unit = fields.Str(required=False, allow_none=True)
    
    shipping = fields.Int(required=False, allow_none=True)
    
    is_default = fields.Boolean(required=False, allow_none=True)
    


class Dimension(BaseSchema):
    # Payment swagger.json

    
    unit = fields.Str(required=False, allow_none=True)
    
    width = fields.Int(required=False, allow_none=True)
    
    height = fields.Int(required=False, allow_none=True)
    
    length = fields.Int(required=False, allow_none=True)
    
    is_default = fields.Boolean(required=False, allow_none=True)
    


class Manufacturer(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False, allow_none=True)
    
    address = fields.Str(required=False, allow_none=True)
    
    is_default = fields.Boolean(required=False, allow_none=True)
    


class ArticleAssignment(BaseSchema):
    # Payment swagger.json

    
    level = fields.Str(required=False, allow_none=True)
    
    strategy = fields.Str(required=False, allow_none=True)
    


class CartUser(BaseSchema):
    # Payment swagger.json

    
    email = fields.Str(required=False, allow_none=True)
    
    gender = fields.Str(required=False, allow_none=True)
    
    mobile = fields.Str(required=False, allow_none=True)
    
    user_id = fields.Str(required=False, allow_none=True)
    
    last_name = fields.Str(required=False, allow_none=True)
    
    user_type = fields.Str(required=False, allow_none=True)
    
    first_name = fields.Str(required=False, allow_none=True)
    
    is_authenticated = fields.Boolean(required=False, allow_none=True)
    


class Affiliate(BaseSchema):
    # Payment swagger.json

    
    id = fields.Str(required=False, allow_none=True)
    
    token = fields.Str(required=False, allow_none=True)
    
    config = fields.Dict(required=False, allow_none=True)
    


class Address(BaseSchema):
    # Payment swagger.json

    
    street = fields.Str(required=False, allow_none=True)
    
    zip = fields.Str(required=False, allow_none=True)
    
    uid = fields.Int(required=False, allow_none=True)
    
    area = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    phone = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    address = fields.Str(required=False, allow_none=True)
    
    country = fields.Str(required=False, allow_none=True)
    
    pincode = fields.Str(required=False, allow_none=True)
    
    landmark = fields.Str(required=False, allow_none=True)
    
    area_code = fields.Str(required=False, allow_none=True)
    
    address_type = fields.Str(required=False, allow_none=True)
    
    country_code = fields.Str(required=False, allow_none=True)
    
    area_code_slug = fields.Str(required=False, allow_none=True)
    
    delivery_address_id = fields.Int(required=False, allow_none=True)
    


class PaymentMethod(BaseSchema):
    # Payment swagger.json

    
    mode = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    


class CardReq(BaseSchema):
    # Payment swagger.json

    
    cart = fields.Nested(CartData, required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    user = fields.Nested(CartUser, required=False)
    
    coupon = fields.Dict(required=False)
    
    affiliate = fields.Nested(Affiliate, required=False)
    
    billing_address = fields.Nested(Address, required=False)
    
    delivery_address = fields.Nested(Address, required=False)
    
    redemption_rules = fields.Dict(required=False, allow_none=True)
    
    payment_identifier = fields.Str(required=False, allow_none=True)
    
    pick_up_customer_details = fields.Dict(required=False, allow_none=True)
    
    payment_auto_confirm = fields.Boolean(required=False, allow_none=True)
    
    payment_methods = fields.List(fields.Nested(PaymentMethod, required=False), required=False)
    
    coupon_id = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    cart_value = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    return_url = fields.Str(required=False)
    
    cashback_id = fields.Str(required=False, allow_none=True)
    
    cod_charges = fields.Int(required=False)
    
    employee_id = fields.Str(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    cashback = fields.Int(required=False)
    
    merchant_code = fields.Str(required=False)
    
    ordering_store = fields.Str(required=False, allow_none=True)
    


class UpdateAggregatorCardReq(BaseSchema):
    # Payment swagger.json

    
    refresh = fields.Boolean(required=False)
    


class UpdateAggregatorCardDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    cards = fields.Nested(AggregatorCard, required=False)
    


class AggregatorCard(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    api = fields.Str(required=False, allow_none=True)
    
    customer_id = fields.Str(required=False, allow_none=True)
    


class UpdateCard(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    


class PaymentCallbackDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class PaymentConfirmation(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    amount = fields.Float(required=False)
    
    mode = fields.Str(required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Payment swagger.json

    
    extra_meta = fields.Dict(required=False, allow_none=True)
    
    order_id = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class PaymentConfirmationDetails(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    errors = fields.Str(required=False)
    
    return_url = fields.Str(required=False)
    


class HttpErrorCodeAndMessage(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    


