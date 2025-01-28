"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class PaymentGatewayConfigResponse(BaseSchema):
    pass


class AggregatorConfig(BaseSchema):
    pass


class DisplayDetails(BaseSchema):
    pass


class PaymentGatewayConfig(BaseSchema):
    pass


class PaymentGatewayConfigRequest(BaseSchema):
    pass


class PaymentGatewayToBeReviewed(BaseSchema):
    pass


class ErrorCodeAndDescription(BaseSchema):
    pass


class HttpErrorCodeAndResponse(BaseSchema):
    pass


class RefundErrorCodeAndResponse(BaseSchema):
    pass


class PaymentOptionErrorCodeAndResponse(BaseSchema):
    pass


class RefundOptionErrorCodeAndResponse(BaseSchema):
    pass


class UserCODAdvanceErrorCodeAndResponse(BaseSchema):
    pass


class UserCodErrorMessage(BaseSchema):
    pass


class RefundOptionMessage(BaseSchema):
    pass


class RefundOptionError(BaseSchema):
    pass


class PaymentOptionError(BaseSchema):
    pass


class PaymentSessionError(BaseSchema):
    pass


class PaymentErrorCodeDescription(BaseSchema):
    pass


class EDCError(BaseSchema):
    pass


class IFSCErrorData(BaseSchema):
    pass


class IntentAppErrorList(BaseSchema):
    pass


class ProductCODData(BaseSchema):
    pass


class CODChargesLimitsResponse(BaseSchema):
    pass


class PaymentModeLogo(BaseSchema):
    pass


class IntentApp(BaseSchema):
    pass


class PaymentModeList(BaseSchema):
    pass


class RootPaymentMode(BaseSchema):
    pass


class Version(BaseSchema):
    pass


class VersionDetails(BaseSchema):
    pass


class PaymentOptions(BaseSchema):
    pass


class PaymentFlowData(BaseSchema):
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


class PaymentModeRouteResponse(BaseSchema):
    pass


class DeliverySlot(BaseSchema):
    pass


class DeliverySlotDetail(BaseSchema):
    pass


class PaymentOptionsResponse(BaseSchema):
    pass


class PayoutCustomer(BaseSchema):
    pass


class PayoutMoreAttributes(BaseSchema):
    pass


class PayoutAggregator(BaseSchema):
    pass


class Payout(BaseSchema):
    pass


class PayoutsResponse(BaseSchema):
    pass


class PayoutBankDetails(BaseSchema):
    pass


class PayoutUserDetails(BaseSchema):
    pass


class PayoutRequest(BaseSchema):
    pass


class PayoutResponse(BaseSchema):
    pass


class PayoutDetails(BaseSchema):
    pass


class BankDetails(BaseSchema):
    pass


class UpdatePayoutResponse(BaseSchema):
    pass


class Payouts(BaseSchema):
    pass


class UpdatePayoutRequest(BaseSchema):
    pass


class DeletePayoutResponse(BaseSchema):
    pass


class RefundAccountResponse(BaseSchema):
    pass


class GetRefundAccountResponse(BaseSchema):
    pass


class NotFoundResourceError(BaseSchema):
    pass


class BankDetailsForOTP(BaseSchema):
    pass


class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    pass


class IfscCodeResponse(BaseSchema):
    pass


class OrderBeneficiaryDetails(BaseSchema):
    pass


class OrderBeneficiaryResponse(BaseSchema):
    pass


class MultiTenderPaymentMeta(BaseSchema):
    pass


class MultiTenderPaymentMethod(BaseSchema):
    pass


class PaymentConfirmationRequest(BaseSchema):
    pass


class PaymentConfirmationResponse(BaseSchema):
    pass


class AdvancePaymentLimitConfig(BaseSchema):
    pass


class CODLimitConfig(BaseSchema):
    pass


class CODPaymentLimitConfig(BaseSchema):
    pass


class UserPaymentLimitConfig(BaseSchema):
    pass


class GetUserBULimitResponse(BaseSchema):
    pass


class GetUserCODLimitResponse(BaseSchema):
    pass


class SetAdvanceLimitConfig(BaseSchema):
    pass


class SetCODLimitConfig(BaseSchema):
    pass


class SetUserPaymentLimitConfig(BaseSchema):
    pass


class SetBUPaymentLimit(BaseSchema):
    pass


class SetCODForUserRequest(BaseSchema):
    pass


class EdcModelData(BaseSchema):
    pass


class EdcAggregatorAndModelListResponse(BaseSchema):
    pass


class StatisticsData(BaseSchema):
    pass


class EdcDeviceStatsResponse(BaseSchema):
    pass


class EdcAddRequest(BaseSchema):
    pass


class EdcDevice(BaseSchema):
    pass


class EdcDeviceAddResponse(BaseSchema):
    pass


class EdcDeviceDetailsResponse(BaseSchema):
    pass


class EdcUpdateRequest(BaseSchema):
    pass


class EdcDeviceUpdateResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class EdcDeviceListResponse(BaseSchema):
    pass


class PaymentInitializationRequest(BaseSchema):
    pass


class PaymentInitializationResponse(BaseSchema):
    pass


class PaymentStatusUpdateRequest(BaseSchema):
    pass


class PaymentStatusUpdateResponse(BaseSchema):
    pass


class ResendOrCancelPaymentRequest(BaseSchema):
    pass


class LinkStatus(BaseSchema):
    pass


class ResendOrCancelPaymentResponse(BaseSchema):
    pass


class PaymentStatusBulkHandlerRequest(BaseSchema):
    pass


class PaymentObjectListSerializer(BaseSchema):
    pass


class PaymentStatusObject(BaseSchema):
    pass


class PaymentStatusBulkHandlerResponse(BaseSchema):
    pass


class GetOauthUrlResponse(BaseSchema):
    pass


class RevokeOAuthToken(BaseSchema):
    pass


class RepaymentRequestDetails(BaseSchema):
    pass


class RepaymentDetailsSerialiserPayAll(BaseSchema):
    pass


class RepaymentResponse(BaseSchema):
    pass


class MerchantOnBoardingRequest(BaseSchema):
    pass


class MerchantOnBoardingResponse(BaseSchema):
    pass


class MerchantOnboardingData(BaseSchema):
    pass


class ValidateCustomerRequest(BaseSchema):
    pass


class MerchantParams(BaseSchema):
    pass


class OrderItems(BaseSchema):
    pass


class ValidateCustomerResponse(BaseSchema):
    pass


class ValidateCustomer(BaseSchema):
    pass


class ValidateCustomerData(BaseSchema):
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


class PollingPaymentLinkResponse(BaseSchema):
    pass


class CancelOrResendPaymentLinkRequest(BaseSchema):
    pass


class ResendPaymentLinkResponse(BaseSchema):
    pass


class PaymentLinkError(BaseSchema):
    pass


class CancelPaymentLinkResponse(BaseSchema):
    pass


class Code(BaseSchema):
    pass


class PaymentCode(BaseSchema):
    pass


class GetPaymentCode(BaseSchema):
    pass


class GetPaymentCodeResponse(BaseSchema):
    pass


class PlatformOnlineOfflinePaymentResponse(BaseSchema):
    pass


class PatchPlatformOnlineOfflinePaymentResponse(BaseSchema):
    pass


class PlatformOnlineOfflineItem(BaseSchema):
    pass


class OnlinePaymentDetails(BaseSchema):
    pass


class OfflinePaymentDetails(BaseSchema):
    pass


class CODOffline(BaseSchema):
    pass


class AggregatorDetails(BaseSchema):
    pass


class CODPaymentMode(BaseSchema):
    pass


class PlatformPaymentModeRequest(BaseSchema):
    pass


class PlatformPaymentModeResponse(BaseSchema):
    pass


class AggregatorPlatformPaymentModeResponse(BaseSchema):
    pass


class PlatformOfflineAdvanceRequest(BaseSchema):
    pass


class PlatformOfflineAdvanceResponse(BaseSchema):
    pass


class OfflineAdvanceConfigurationItem(BaseSchema):
    pass


class OfflineAdvanceDevice(BaseSchema):
    pass


class OfflineAdvanceConfig(BaseSchema):
    pass


class PaymentModeItem(BaseSchema):
    pass


class MerchantPaymentModeRequest(BaseSchema):
    pass


class ModeIsactive(BaseSchema):
    pass


class OfferSerializer(BaseSchema):
    pass


class AppliedOfferSerializer(BaseSchema):
    pass


class OrderDetail(BaseSchema):
    pass


class AggregatorOrderDetail(BaseSchema):
    pass


class GoogleMapPoint(BaseSchema):
    pass


class AddressDetail(BaseSchema):
    pass


class LatLongDetail(BaseSchema):
    pass


class PaymentSessionDetail(BaseSchema):
    pass


class RefundDetailsSerializer(BaseSchema):
    pass


class AmountSerializer(BaseSchema):
    pass


class ChargeAmountSerializer(BaseSchema):
    pass


class CartChargesSerializer(BaseSchema):
    pass


class CartDetailsSerializer(BaseSchema):
    pass


class GetPaymentSessionResponse(BaseSchema):
    pass


class PaymentSessionRequestSerializer(BaseSchema):
    pass


class TransactionDetail(BaseSchema):
    pass


class PaymentSessionResponseSerializer(BaseSchema):
    pass


class RefundSessionDetail(BaseSchema):
    pass


class RefundSessionRequestSerializer(BaseSchema):
    pass


class RefundSessionResponseSerializer(BaseSchema):
    pass


class RefundSourcesPriority(BaseSchema):
    pass


class RefundPriorityResponseSerializer(BaseSchema):
    pass


class RefundPriorityRequestSerializer(BaseSchema):
    pass


class FromConfig(BaseSchema):
    pass


class ToConfig(BaseSchema):
    pass


class PlatformPaymentModeCopyConfigRequest(BaseSchema):
    pass


class PaymentMethodsMetaOrder(BaseSchema):
    pass


class PaymentOrderMethods(BaseSchema):
    pass


class PaymentOrderRequest(BaseSchema):
    pass


class CustomerDetails(BaseSchema):
    pass


class PaymentOrderData(BaseSchema):
    pass


class PaymentOrderResponse(BaseSchema):
    pass


class AggregatorVersionItemSchema(BaseSchema):
    pass


class AggregatorVersionResponse(BaseSchema):
    pass


class AggregatorVersionRequestSchema(BaseSchema):
    pass


class AggregatorControlRequest(BaseSchema):
    pass


class PaymentModeCustomConfigSchema(BaseSchema):
    pass


class PaymentCustomConfigDetailsSchema(BaseSchema):
    pass


class PaymentCustomConfigCustomerSchema(BaseSchema):
    pass


class PaymentCustomConfigModeSchema(BaseSchema):
    pass


class PaymentCustomConfigDetailsRequestSchema(BaseSchema):
    pass


class PaymentCustomConfigCustomerRequestSchema(BaseSchema):
    pass


class PaymentCustomConfigRequestSchema(BaseSchema):
    pass


class PaymentCustomConfigResponseSchema(BaseSchema):
    pass


class DeleteBeneficiaryRequest(BaseSchema):
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


class TransferMode(BaseSchema):
    pass


class WalletBeneficiaryDetails(BaseSchema):
    pass


class UpiBeneficiaryDetails(BaseSchema):
    pass


class BeneficiaryRefundOptions(BaseSchema):
    pass


class OrderBeneficiaryResponseSchemaV2(BaseSchema):
    pass


class RefundOptionsLimit(BaseSchema):
    pass


class ValidateValidateAddressRequest(BaseSchema):
    pass


class VPADetails(BaseSchema):
    pass


class ValidateValidateAddressResponse(BaseSchema):
    pass


class SetDefaultBeneficiaryRequest(BaseSchema):
    pass


class SetDefaultBeneficiaryResponse(BaseSchema):
    pass


class ShipmentRefundRequestMeta(BaseSchema):
    pass


class ShipmentRefundRequest(BaseSchema):
    pass


class ShipmentRefundDetail(BaseSchema):
    pass


class ShipmentRefundResponse(BaseSchema):
    pass


class RefundOptionsPriority(BaseSchema):
    pass


class RefundItem(BaseSchema):
    pass


class PennyDropValidationResponse(BaseSchema):
    pass


class UpdatePennyDropValidationRequest(BaseSchema):
    pass


class AggregatorConfigResponse(BaseSchema):
    pass


class PaymentModeResponse(BaseSchema):
    pass


class PaymentOptionItem(BaseSchema):
    pass


class PaymentMode(BaseSchema):
    pass


class SubPaymentMode(BaseSchema):
    pass


class AggregatorCredentialRequest(BaseSchema):
    pass


class PatchAggregatorCredentialResponse(BaseSchema):
    pass


class AggregatorCredentialResponse(BaseSchema):
    pass


class AggregatorCredential(BaseSchema):
    pass


class AggregatorDisplayItem(BaseSchema):
    pass


class GetDeviceResponse(BaseSchema):
    pass


class BusinessUnitDevice(BaseSchema):
    pass


class BusinessUnit(BaseSchema):
    pass


class Device(BaseSchema):
    pass


class AggregatorHistoryResponse(BaseSchema):
    pass


class HistoryItem(BaseSchema):
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


class PaymentMethodConfigResponse(BaseSchema):
    pass


class RequiredSessionPath(BaseSchema):
    pass


class SessionItem(BaseSchema):
    pass


class PaymentErrorCodeAndResponse(BaseSchema):
    pass


class PaymentError(BaseSchema):
    pass


class ShipmentBeneficiaryDetailsResponse(BaseSchema):
    pass





class PaymentGatewayConfigResponse(BaseSchema):
    # Payment swagger.json

    
    aggregators = fields.List(fields.Nested(AggregatorConfig, required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    
    display_fields = fields.List(fields.Str(required=False), required=False)
    


class AggregatorConfig(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    config_type = fields.Str(required=False)
    
    display = fields.Nested(DisplayDetails, required=False)
    
    aggregator = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class DisplayDetails(BaseSchema):
    # Payment swagger.json

    
    link = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    review_status = fields.Str(required=False)
    
    info = fields.List(fields.Str(required=False, allow_none=True), required=False)
    


class PaymentGatewayConfig(BaseSchema):
    # Payment swagger.json

    
    secret = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    key = fields.Str(required=False)
    
    merchant_salt = fields.Str(required=False)
    


class PaymentGatewayConfigRequest(BaseSchema):
    # Payment swagger.json

    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    ccavenue = fields.Nested(PaymentGatewayConfig, required=False)
    
    razorpay = fields.Nested(PaymentGatewayConfig, required=False)
    
    juspay = fields.Nested(PaymentGatewayConfig, required=False)
    


class PaymentGatewayToBeReviewed(BaseSchema):
    # Payment swagger.json

    
    aggregators = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class HttpErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Str(required=False), required=False)
    
    message = fields.Str(required=False)
    


class RefundErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(IFSCErrorData, required=False)
    
    error = fields.Nested(EDCError, required=False)
    


class PaymentOptionErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.List(fields.Str(required=False), required=False)
    


class RefundOptionErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Nested(RefundOptionMessage, required=False)
    
    error = fields.Nested(RefundOptionError, required=False)
    


class UserCODAdvanceErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(UserCodErrorMessage, required=False)
    


class UserCodErrorMessage(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    description = fields.Nested(RefundOptionError, required=False)
    


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
    


class PaymentOptionError(BaseSchema):
    # Payment swagger.json

    
    option_type = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.List(fields.Str(required=False), required=False)
    
    checksum = fields.List(fields.Str(required=False), required=False)
    


class PaymentSessionError(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(PaymentErrorCodeDescription, required=False)
    


class PaymentErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    description = fields.Nested(PaymentOptionError, required=False)
    
    code = fields.Str(required=False)
    


class EDCError(BaseSchema):
    # Payment swagger.json

    
    error = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class IFSCErrorData(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    subcode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class IntentAppErrorList(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    


class ProductCODData(BaseSchema):
    # Payment swagger.json

    
    items = fields.Dict(required=False, allow_none=True)
    
    cod_charges = fields.Nested(CODChargesLimitsResponse, required=False)
    


class CODChargesLimitsResponse(BaseSchema):
    # Payment swagger.json

    
    max_cart_value = fields.Float(required=False, allow_none=True)
    
    min_cart_value = fields.Float(required=False, allow_none=True)
    
    cod_charge = fields.Float(required=False, allow_none=True)
    


class PaymentModeLogo(BaseSchema):
    # Payment swagger.json

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    


class IntentApp(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False, allow_none=True)
    
    display_name = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    


class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    logo = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    bank_code = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    wallet_name = fields.Str(required=False)
    
    wallet_code = fields.Str(required=False)
    
    wallet_id = fields.Int(required=False)
    
    collect_flow = fields.Boolean(required=False)
    
    provider = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
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

    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    display_priority = fields.Int(required=False)
    
    add_card_enabled = fields.Boolean(required=False, allow_none=True)
    
    save_card = fields.Boolean(required=False, allow_none=True)
    
    is_pay_by_card_pl = fields.Boolean(required=False, allow_none=True)
    
    display_name = fields.Str(required=False)
    
    anonymous_enable = fields.Boolean(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    payment_mode_id = fields.Int(required=False, allow_none=True)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    version = fields.Nested(Version, required=False)
    
    aggregator_name = fields.Str(required=False, allow_none=True)
    


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
    


class PaymentOptions(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    


class PaymentFlowData(BaseSchema):
    # Payment swagger.json

    
    is_customer_validation_required = fields.Boolean(required=False)
    
    cust_validation_url = fields.Str(required=False, allow_none=True)
    
    config = fields.Nested(PaymentConfig, required=False)
    
    data = fields.Nested(GatewayData, required=False)
    
    return_url = fields.Str(required=False, allow_none=True)
    


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
    


class PaymentOptionAndFlow(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    


class AdvanceObject(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    
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
    


class PaymentModeRouteResponse(BaseSchema):
    # Payment swagger.json

    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    
    success = fields.Boolean(required=False)
    
    payment_breakup = fields.Dict(required=False)
    
    advance_payment = fields.List(fields.Nested(AdvancePaymentObject, required=False), required=False)
    
    delivery_charges = fields.Float(required=False)
    
    store_code = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    cod_message = fields.Str(required=False)
    
    delivery_slots = fields.List(fields.Nested(DeliverySlot, required=False), required=False)
    
    user_type = fields.Str(required=False)
    
    cod_available = fields.Boolean(required=False)
    
    cod_charges = fields.Int(required=False)
    
    max_cart_value = fields.Int(required=False)
    
    min_cart_value = fields.Int(required=False)
    
    store_emp_list = fields.List(fields.Str(required=False), required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    cod_limit = fields.Int(required=False)
    
    remaining_limit = fields.Float(required=False)
    
    cod_limit_per_order = fields.Int(required=False)
    
    product_cod_data = fields.Dict(required=False)
    
    is_product_cod_available = fields.Boolean(required=False)
    
    is_pincode_cod_available = fields.Boolean(required=False)
    


class DeliverySlot(BaseSchema):
    # Payment swagger.json

    
    date = fields.Str(required=False)
    
    delivery_slot = fields.List(fields.Nested(DeliverySlotDetail, required=False), required=False)
    


class DeliverySlotDetail(BaseSchema):
    # Payment swagger.json

    
    delivery_slot_timing = fields.Str(required=False)
    
    delivery_slot_id = fields.Int(required=False)
    


class PaymentOptionsResponse(BaseSchema):
    # Payment swagger.json

    
    payment_options = fields.Nested(PaymentOptions, required=False)
    
    success = fields.Boolean(required=False)
    
    payment_breakup = fields.Dict(required=False)
    


class PayoutCustomer(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False, allow_none=True)
    
    mobile = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    id = fields.Int(required=False, allow_none=True)
    


class PayoutMoreAttributes(BaseSchema):
    # Payment swagger.json

    
    branch_name = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    account_no = fields.Str(required=False, allow_none=True)
    
    country = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    account_holder = fields.Str(required=False, allow_none=True)
    
    ifsc_code = fields.Str(required=False, allow_none=True)
    
    account_type = fields.Str(required=False, allow_none=True)
    
    bank_name = fields.Str(required=False, allow_none=True)
    


class PayoutAggregator(BaseSchema):
    # Payment swagger.json

    
    aggregator_id = fields.Int(required=False, allow_none=True)
    
    aggregator_fund_id = fields.Int(required=False, allow_none=True)
    
    payout_details_id = fields.Int(required=False, allow_none=True)
    


class Payout(BaseSchema):
    # Payment swagger.json

    
    customers = fields.Nested(PayoutCustomer, required=False)
    
    more_attributes = fields.Nested(PayoutMoreAttributes, required=False)
    
    is_default = fields.Boolean(required=False)
    
    payouts_aggregators = fields.List(fields.Nested(PayoutAggregator, required=False), required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    


class PayoutsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(Payout, required=False), required=False)
    


class PayoutBankDetails(BaseSchema):
    # Payment swagger.json

    
    ifsc_code = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    


class PayoutUserDetails(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class PayoutRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    users = fields.Nested(PayoutUserDetails, required=False)
    
    unique_external_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    transfer_type = fields.Str(required=False)
    


class PayoutResponse(BaseSchema):
    # Payment swagger.json

    
    payment_status = fields.Str(required=False)
    
    users = fields.Nested(PayoutUserDetails, required=False)
    
    aggregator = fields.Str(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    success = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    created = fields.Boolean(required=False)
    
    payouts = fields.Nested(PayoutDetails, required=False)
    


class PayoutDetails(BaseSchema):
    # Payment swagger.json

    
    more_attributes = fields.Nested(BankDetails, required=False)
    
    aggregator_fund_id = fields.Str(required=False, allow_none=True)
    


class BankDetails(BaseSchema):
    # Payment swagger.json

    
    account_type = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    aggregator_fund_id = fields.Str(required=False)
    


class UpdatePayoutResponse(BaseSchema):
    # Payment swagger.json

    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    transfer_type = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    users = fields.Nested(PayoutUserDetails, required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    updated = fields.Boolean(required=False)
    
    payment_status = fields.Str(required=False)
    
    payouts = fields.Nested(Payouts, required=False)
    


class Payouts(BaseSchema):
    # Payment swagger.json

    
    aggregator_fund_id = fields.Str(required=False, allow_none=True)
    


class UpdatePayoutRequest(BaseSchema):
    # Payment swagger.json

    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    unique_external_id = fields.Str(required=False)
    


class DeletePayoutResponse(BaseSchema):
    # Payment swagger.json

    
    delete = fields.Boolean(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class RefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class GetRefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.List(fields.Nested(BankDetailsForOTP, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class NotFoundResourceError(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class BankDetailsForOTP(BaseSchema):
    # Payment swagger.json

    
    ifsc_code = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    


class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    delights = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    


class IfscCodeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    branch_name = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    


class OrderBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    subtitle = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False, allow_none=True)
    
    transfer_mode = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    branch_name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    aggregator_id = fields.Int(required=False, allow_none=True)
    
    is_verified = fields.Boolean(required=False, allow_none=True)
    
    status = fields.Str(required=False, allow_none=True)
    
    txn_id = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    bank_name = fields.Str(required=False, allow_none=True)
    
    account_no = fields.Str(required=False, allow_none=True)
    
    mobile = fields.Str(required=False, allow_none=True)
    
    default_beneficiary = fields.Boolean(required=False, allow_none=True)
    


class OrderBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    
    bank = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Payment swagger.json

    
    extra_meta = fields.Dict(required=False, allow_none=True)
    
    order_id = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    amount = fields.Float(required=False)
    
    mode = fields.Str(required=False)
    


class PaymentConfirmationRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    


class PaymentConfirmationResponse(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    errors = fields.Str(required=False)
    
    return_url = fields.Str(required=False)
    


class AdvancePaymentLimitConfig(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    prepayment_type = fields.Str(required=False)
    
    prepayment_value = fields.Float(required=False)
    
    cancellation_type = fields.Str(required=False)
    
    all_cancellation_type = fields.List(fields.Str(required=False), required=False)
    
    all_prepayment_type = fields.List(fields.Str(required=False), required=False)
    


class CODLimitConfig(BaseSchema):
    # Payment swagger.json

    
    storefront = fields.Float(required=False)
    
    pos = fields.Float(required=False)
    


class CODPaymentLimitConfig(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    usages = fields.Float(required=False)
    
    user_id = fields.Int(required=False)
    
    merchant_user_id = fields.Str(required=False)
    
    remaining_limit = fields.Int(required=False)
    
    limit = fields.Nested(CODLimitConfig, required=False)
    


class UserPaymentLimitConfig(BaseSchema):
    # Payment swagger.json

    
    advance = fields.Nested(AdvancePaymentLimitConfig, required=False)
    
    cod = fields.Nested(CODPaymentLimitConfig, required=False)
    


class GetUserBULimitResponse(BaseSchema):
    # Payment swagger.json

    
    buisness_unit = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    config = fields.Nested(UserPaymentLimitConfig, required=False)
    


class GetUserCODLimitResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(GetUserBULimitResponse, required=False), required=False)
    


class SetAdvanceLimitConfig(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    prepayment_type = fields.Str(required=False)
    
    prepayment_value = fields.Float(required=False)
    
    cancellation_type = fields.Str(required=False)
    
    all_cancellation_type = fields.List(fields.Str(required=False), required=False)
    


class SetCODLimitConfig(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    usages = fields.Float(required=False)
    
    user_id = fields.Int(required=False)
    
    merchant_user_id = fields.Str(required=False)
    
    limit = fields.Nested(CODLimitConfig, required=False)
    
    remaining_limit = fields.Float(required=False)
    


class SetUserPaymentLimitConfig(BaseSchema):
    # Payment swagger.json

    
    advance = fields.Nested(SetAdvanceLimitConfig, required=False)
    
    cod = fields.Nested(SetCODLimitConfig, required=False)
    


class SetBUPaymentLimit(BaseSchema):
    # Payment swagger.json

    
    buisness_unit = fields.Str(required=False)
    
    config = fields.Nested(SetUserPaymentLimitConfig, required=False)
    


class SetCODForUserRequest(BaseSchema):
    # Payment swagger.json

    
    mobile_no = fields.Str(required=False)
    
    merchant_user_id = fields.Str(required=False)
    
    items = fields.List(fields.Nested(SetBUPaymentLimit, required=False), required=False)
    


class EdcModelData(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    models = fields.List(fields.Str(required=False), required=False)
    


class EdcAggregatorAndModelListResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(EdcModelData, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class StatisticsData(BaseSchema):
    # Payment swagger.json

    
    inactive_device_count = fields.Int(required=False)
    
    active_device_count = fields.Int(required=False)
    


class EdcDeviceStatsResponse(BaseSchema):
    # Payment swagger.json

    
    statistics = fields.Nested(StatisticsData, required=False)
    
    success = fields.Boolean(required=False)
    


class EdcAddRequest(BaseSchema):
    # Payment swagger.json

    
    edc_model = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    
    terminal_serial_no = fields.Str(required=False)
    
    device_tag = fields.Str(required=False, allow_none=True)
    


class EdcDevice(BaseSchema):
    # Payment swagger.json

    
    edc_model = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    terminal_unique_identifier = fields.Str(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    terminal_serial_no = fields.Str(required=False)
    
    merchant_store_pos_code = fields.Str(required=False, allow_none=True)
    
    device_tag = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    


class EdcDeviceAddResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EdcDevice, required=False)
    
    success = fields.Boolean(required=False)
    


class EdcDeviceDetailsResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EdcDevice, required=False)
    
    success = fields.Boolean(required=False)
    


class EdcUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    edc_model = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    merchant_store_pos_code = fields.Str(required=False)
    
    device_tag = fields.Str(required=False, allow_none=True)
    


class EdcDeviceUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    


class Page(BaseSchema):
    # Payment swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class EdcDeviceListResponse(BaseSchema):
    # Payment swagger.json

    
    items = fields.List(fields.Nested(EdcDevice, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentInitializationRequest(BaseSchema):
    # Payment swagger.json

    
    razorpay_payment_id = fields.Str(required=False, allow_none=True)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    amount = fields.Int(required=False, allow_none=True)
    
    contact = fields.Str(required=False)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    


class PaymentInitializationResponse(BaseSchema):
    # Payment swagger.json

    
    razorpay_payment_id = fields.Str(required=False, allow_none=True)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    upi_poll_url = fields.Str(required=False, allow_none=True)
    
    customer_id = fields.Str(required=False, allow_none=True)
    
    polling_url = fields.Str(required=False)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    currency = fields.Str(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    amount = fields.Int(required=False, allow_none=True)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    virtual_id = fields.Str(required=False, allow_none=True)
    
    bqr_image = fields.Str(required=False, allow_none=True)
    
    aggregator_order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    method = fields.Str(required=False)
    


class PaymentStatusUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    device_id = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    amount = fields.Int(required=False, allow_none=True)
    
    contact = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    unique_link_id = fields.Str(required=False)
    


class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    redirect_url = fields.Str(required=False, allow_none=True)
    
    retry = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    status = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    


class ResendOrCancelPaymentRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    request_type = fields.Str(required=False)
    


class LinkStatus(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class ResendOrCancelPaymentResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(LinkStatus, required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentStatusBulkHandlerRequest(BaseSchema):
    # Payment swagger.json

    
    merchant_order_id = fields.List(fields.Str(required=False), required=False)
    


class PaymentObjectListSerializer(BaseSchema):
    # Payment swagger.json

    
    user_object = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    collected_by = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    refund_object = fields.Dict(required=False, allow_none=True)
    
    id = fields.Str(required=False)
    
    payment_id = fields.Str(required=False, allow_none=True)
    
    currency = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    aggregator_payment_object = fields.Dict(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False)
    
    refunded_by = fields.Str(required=False)
    
    amount_in_paisa = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    payment_mode_identifier = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    all_status = fields.List(fields.Str(required=False), required=False)
    


class PaymentStatusObject(BaseSchema):
    # Payment swagger.json

    
    merchant_order_id = fields.Str(required=False)
    
    payment_object_list = fields.List(fields.Nested(PaymentObjectListSerializer, required=False), required=False)
    


class PaymentStatusBulkHandlerResponse(BaseSchema):
    # Payment swagger.json

    
    count = fields.Int(required=False)
    
    data = fields.List(fields.Nested(PaymentStatusObject, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class GetOauthUrlResponse(BaseSchema):
    # Payment swagger.json

    
    url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class RevokeOAuthToken(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class RepaymentRequestDetails(BaseSchema):
    # Payment swagger.json

    
    fwd_shipment_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    payment_mode = fields.Str(required=False)
    
    outstanding_details_id = fields.Int(required=False)
    
    aggregator_transaction_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    payment_mode_identifier = fields.Str(required=False)
    


class RepaymentDetailsSerialiserPayAll(BaseSchema):
    # Payment swagger.json

    
    total_amount = fields.Float(required=False)
    
    extension_order_id = fields.Str(required=False, allow_none=True)
    
    aggregator_transaction_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    shipment_details = fields.List(fields.Nested(RepaymentRequestDetails, required=False), required=False)
    


class RepaymentResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class MerchantOnBoardingRequest(BaseSchema):
    # Payment swagger.json

    
    credit_line_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class MerchantOnBoardingResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(MerchantOnboardingData, required=False)
    
    success = fields.Boolean(required=False)
    


class MerchantOnboardingData(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    


class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    phone_number = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    payload = fields.Str(required=False, allow_none=True)
    
    delivery_address = fields.Nested(AddressDetail, required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    order_items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    merchant_params = fields.Nested(MerchantParams, required=False)
    
    billing_address = fields.Nested(AddressDetail, required=False)
    


class MerchantParams(BaseSchema):
    # Payment swagger.json

    
    source = fields.Str(required=False)
    


class OrderItems(BaseSchema):
    # Payment swagger.json

    
    sku = fields.Str(required=False)
    
    price = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class ValidateCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(ValidateCustomer, required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ValidateCustomer, required=False)
    


class ValidateCustomer(BaseSchema):
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
    


class GetPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    currency = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    amount = fields.Float(required=False, allow_none=True)
    
    merchant_name = fields.Str(required=False, allow_none=True)
    
    payment_link_url = fields.Str(required=False, allow_none=True)
    
    payment_link_current_status = fields.Str(required=False, allow_none=True)
    
    external_order_id = fields.Str(required=False, allow_none=True)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    


class ErrorDescription(BaseSchema):
    # Payment swagger.json

    
    msg = fields.Str(required=False, allow_none=True)
    
    payment_transaction_id = fields.Str(required=False, allow_none=True)
    
    invalid_id = fields.Boolean(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False, allow_none=True)
    
    merchant_name = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    
    expired = fields.Boolean(required=False, allow_none=True)
    
    cancelled = fields.Boolean(required=False, allow_none=True)
    
    description = fields.Str(required=False, allow_none=True)
    


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
    
    amount = fields.Str(required=False)
    
    assign_card_id = fields.Str(required=False, allow_none=True)
    
    pincode = fields.Str(required=False, allow_none=True)
    


class CreatePaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    email = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    mobile_number = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    external_order_id = fields.Str(required=False)
    


class CreatePaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    payment_link_url = fields.Str(required=False, allow_none=True)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    payment_link_id = fields.Str(required=False, allow_none=True)
    


class PollingPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    http_status = fields.Int(required=False, allow_none=True)
    
    status_code = fields.Int(required=False, allow_none=True)
    
    redirect_url = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    payment_link_id = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False, allow_none=True)
    
    aggregator_name = fields.Str(required=False, allow_none=True)
    
    error = fields.Str(required=False)
    


class CancelOrResendPaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    


class ResendPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(PaymentLinkError, required=False)
    


class PaymentLinkError(BaseSchema):
    # Payment swagger.json

    
    cancelled = fields.Boolean(required=False)
    
    msg = fields.Str(required=False)
    


class CancelPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(PaymentLinkError, required=False)
    


class Code(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class PaymentCode(BaseSchema):
    # Payment swagger.json

    
    codes = fields.List(fields.Nested(Code, required=False), required=False)
    
    name = fields.Str(required=False)
    
    networks = fields.List(fields.Str(required=False), required=False)
    
    types = fields.List(fields.Str(required=False), required=False)
    


class GetPaymentCode(BaseSchema):
    # Payment swagger.json

    
    cod = fields.Nested(PaymentCode, required=False)
    
    nb = fields.Nested(PaymentCode, required=False)
    
    wl = fields.Nested(PaymentCode, required=False)
    
    card = fields.Nested(PaymentCode, required=False)
    
    pl = fields.Nested(PaymentCode, required=False)
    
    ps = fields.Nested(PaymentCode, required=False)
    
    op = fields.Nested(PaymentCode, required=False)
    
    upi = fields.Nested(PaymentCode, required=False)
    
    qr = fields.Nested(PaymentCode, required=False)
    
    fc = fields.Nested(PaymentCode, required=False)
    
    pac = fields.Nested(PaymentCode, required=False)
    
    stripepg = fields.Nested(PaymentCode, required=False)
    
    payumoneypg = fields.Nested(PaymentCode, required=False)
    
    rupifipg = fields.Nested(PaymentCode, required=False)
    
    cas = fields.Nested(PaymentCode, required=False)
    
    csas = fields.Nested(PaymentCode, required=False)
    
    ccavenuepg = fields.Nested(PaymentCode, required=False)
    
    cardless_emi = fields.Nested(PaymentCode, required=False)
    
    cashback = fields.Nested(PaymentCode, required=False)
    
    loyalty = fields.Nested(PaymentCode, required=False)
    
    employee_discount = fields.Nested(PaymentCode, required=False)
    
    paymentlink = fields.Nested(PaymentCode, required=False)
    
    epaylater = fields.Nested(PaymentCode, required=False)
    
    udhaari = fields.Nested(PaymentCode, required=False)
    
    creditnote = fields.Nested(PaymentCode, required=False)
    
    checkout = fields.Nested(PaymentCode, required=False)
    
    rone = fields.Nested(PaymentCode, required=False)
    
    emi = fields.Nested(PaymentCode, required=False)
    
    sodexo = fields.Nested(PaymentCode, required=False)
    
    jm_wallet = fields.Nested(PaymentCode, required=False)
    


class GetPaymentCodeResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(GetPaymentCode, required=False)
    
    success = fields.Boolean(required=False)
    


class PlatformOnlineOfflinePaymentResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    items = fields.Nested(PlatformOnlineOfflineItem, required=False)
    
    success = fields.Boolean(required=False)
    


class PatchPlatformOnlineOfflinePaymentResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    items = fields.List(fields.Nested(PlatformOnlineOfflineItem, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class PlatformOnlineOfflineItem(BaseSchema):
    # Payment swagger.json

    
    online = fields.Nested(OnlinePaymentDetails, required=False)
    
    offline = fields.Nested(OfflinePaymentDetails, required=False)
    
    advance = fields.Nested(PlatformOfflineAdvanceResponse, required=False)
    


class OnlinePaymentDetails(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    aggregators = fields.List(fields.Nested(AggregatorDetails, required=False), required=False)
    


class OfflinePaymentDetails(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    payment_modes = fields.Nested(CODOffline, required=False)
    


class CODOffline(BaseSchema):
    # Payment swagger.json

    
    cod = fields.Nested(CODPaymentMode, required=False)
    


class AggregatorDetails(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    integration_type = fields.Str(required=False)
    
    config = fields.List(fields.Str(required=False), required=False)
    
    extension_id = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False)
    
    is_tnc_accepted = fields.Boolean(required=False)
    
    label = fields.Str(required=False)
    


class CODPaymentMode(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    is_active = fields.Boolean(required=False)
    


class PlatformPaymentModeRequest(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.Str(required=False)
    
    device = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(PaymentModeItem, required=False), required=False)
    


class PlatformPaymentModeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    business_unit = fields.Str(required=False)
    
    device = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(PaymentOptionItem, required=False), required=False)
    


class AggregatorPlatformPaymentModeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    business_unit = fields.Str(required=False)
    
    device = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    save_allowed = fields.Boolean(required=False)
    
    extension_id = fields.Str(required=False, allow_none=True)
    
    items = fields.List(fields.Nested(PaymentOptionItem, required=False), required=False)
    


class PlatformOfflineAdvanceRequest(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.Str(required=False)
    
    items = fields.List(fields.Nested(OfflineAdvanceConfig, required=False), required=False)
    
    device = fields.Nested(OfflineAdvanceDevice, required=False)
    


class PlatformOfflineAdvanceResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(OfflineAdvanceConfigurationItem, required=False), required=False)
    
    errors = fields.Nested(ErrorCodeAndDescription, required=False)
    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    


class OfflineAdvanceConfigurationItem(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    business_unit = fields.Str(required=False)
    
    config = fields.Nested(OfflineAdvanceConfig, required=False)
    
    device = fields.Nested(OfflineAdvanceDevice, required=False)
    


class OfflineAdvanceDevice(BaseSchema):
    # Payment swagger.json

    
    android = fields.Boolean(required=False)
    
    ios = fields.Boolean(required=False)
    
    desktop = fields.Boolean(required=False)
    


class OfflineAdvanceConfig(BaseSchema):
    # Payment swagger.json

    
    anonymous = fields.Boolean(required=False)
    
    user_limit = fields.Int(required=False, allow_none=True)
    
    charges = fields.Int(required=False)
    
    charges_max_value = fields.Int(required=False)
    
    charges_min_value = fields.Int(required=False)
    
    max_order_value = fields.Int(required=False)
    
    min_order_value = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    number_of_split = fields.Float(required=False)
    
    slug = fields.Str(required=False)
    
    save_allowed = fields.Boolean(required=False)
    
    prepayment_type = fields.Str(required=False)
    
    prepayment_value = fields.Int(required=False)
    
    refund_time_limit = fields.Int(required=False)
    
    time_unit = fields.Str(required=False)
    
    cancellation_type = fields.Str(required=False)
    
    all_cancellation_type = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
    allow_custom_advance_amount = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class PaymentModeItem(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    sub_payment_mode = fields.List(fields.Nested(SubPaymentMode, required=False), required=False)
    


class MerchantPaymentModeRequest(BaseSchema):
    # Payment swagger.json

    
    offline = fields.Nested(ModeIsactive, required=False)
    
    online = fields.Nested(ModeIsactive, required=False)
    


class ModeIsactive(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    


class OfferSerializer(BaseSchema):
    # Payment swagger.json

    
    offer_amount = fields.Float(required=False)
    
    offer_code = fields.Str(required=False)
    
    offer_description = fields.Str(required=False)
    
    offer_id = fields.Str(required=False)
    


class AppliedOfferSerializer(BaseSchema):
    # Payment swagger.json

    
    total_applied_offer_amount = fields.Float(required=False)
    
    offer_list = fields.List(fields.Nested(OfferSerializer, required=False), required=False)
    


class OrderDetail(BaseSchema):
    # Payment swagger.json

    
    gid = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    aggregator_order_details = fields.Nested(AggregatorOrderDetail, required=False)
    
    aggregator = fields.Str(required=False)
    


class AggregatorOrderDetail(BaseSchema):
    # Payment swagger.json

    
    aggregator_order_id = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class GoogleMapPoint(BaseSchema):
    # Payment swagger.json

    
    address = fields.Str(required=False)
    
    sub_locality = fields.Str(required=False)
    


class AddressDetail(BaseSchema):
    # Payment swagger.json

    
    line1 = fields.Str(required=False)
    
    line2 = fields.Str(required=False)
    
    google_map_point = fields.Nested(GoogleMapPoint, required=False)
    
    landmark = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    expire_at = fields.Str(required=False)
    
    geo_location = fields.Dict(required=False)
    
    state = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    g_address_id = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    address_type = fields.Str(required=False, allow_none=True)
    
    address = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    tags = fields.List(fields.Dict(required=False), required=False)
    
    pincode = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class LatLongDetail(BaseSchema):
    # Payment swagger.json

    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class PaymentSessionDetail(BaseSchema):
    # Payment swagger.json

    
    payment_id = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    success_url = fields.Str(required=False)
    
    shipping_address = fields.Nested(AddressDetail, required=False)
    
    amount_captured = fields.Int(required=False)
    
    amount_refunded = fields.Int(required=False)
    
    aggregator_customer_id = fields.Str(required=False)
    
    cancel_url = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMode, required=False), required=False)
    
    created = fields.Str(required=False)
    
    g_user_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    merchant_locale = fields.Str(required=False)
    
    locale = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    gid = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
    billing_address = fields.Nested(AddressDetail, required=False)
    
    captured = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    


class RefundDetailsSerializer(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    created = fields.Str(required=False)
    
    refund_utr = fields.Str(required=False)
    


class AmountSerializer(BaseSchema):
    # Payment swagger.json

    
    value = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    


class ChargeAmountSerializer(BaseSchema):
    # Payment swagger.json

    
    ordering_currency = fields.Nested(AmountSerializer, required=False)
    
    base_currency = fields.Nested(AmountSerializer, required=False)
    


class CartChargesSerializer(BaseSchema):
    # Payment swagger.json

    
    charge_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    amount = fields.Nested(ChargeAmountSerializer, required=False)
    


class CartDetailsSerializer(BaseSchema):
    # Payment swagger.json

    
    items = fields.Dict(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    cart_value = fields.Float(required=False)
    
    cart_charges = fields.List(fields.Nested(CartChargesSerializer, required=False), required=False)
    
    total_quantity = fields.Int(required=False)
    


class GetPaymentSessionResponse(BaseSchema):
    # Payment swagger.json

    
    meta = fields.Dict(required=False)
    
    gid = fields.Str(required=False)
    
    applied_payment_offers = fields.Nested(AppliedOfferSerializer, required=False)
    
    checksum = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    payment_details = fields.Nested(PaymentSessionDetail, required=False)
    
    cart_details = fields.Nested(CartDetailsSerializer, required=False)
    
    total_amount = fields.Int(required=False)
    
    refund_details = fields.List(fields.Nested(RefundDetailsSerializer, required=False), required=False)
    


class PaymentSessionRequestSerializer(BaseSchema):
    # Payment swagger.json

    
    meta = fields.Dict(required=False)
    
    gid = fields.Str(required=False)
    
    applied_payment_offers = fields.Nested(AppliedOfferSerializer, required=False)
    
    checksum = fields.Str(required=False)
    
    order_details = fields.Nested(OrderDetail, required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    payment_details = fields.List(fields.Nested(PaymentSessionDetail, required=False), required=False)
    
    total_amount = fields.Int(required=False)
    


class TransactionDetail(BaseSchema):
    # Payment swagger.json

    
    transaction_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    payment_id = fields.Str(required=False)
    


class PaymentSessionResponseSerializer(BaseSchema):
    # Payment swagger.json

    
    gid = fields.Str(required=False)
    
    platform_transaction_details = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    total_amount = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    transaction_details = fields.List(fields.Nested(TransactionDetail, required=False), required=False)
    


class RefundSessionDetail(BaseSchema):
    # Payment swagger.json

    
    refund_utr = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    reason = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    created = fields.Str(required=False)
    
    source_transfer_reversal = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    transfer_reversal = fields.Str(required=False)
    
    balance_transaction = fields.Str(required=False)
    


class RefundSessionRequestSerializer(BaseSchema):
    # Payment swagger.json

    
    meta = fields.Dict(required=False)
    
    gid = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    payment_details = fields.Nested(PaymentSessionDetail, required=False)
    
    checksum = fields.Str(required=False)
    
    total_amount = fields.Int(required=False)
    
    refund_details = fields.List(fields.Nested(RefundSessionDetail, required=False), required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    
    message = fields.Str(required=False)
    


class RefundSessionResponseSerializer(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    gid = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    platform_refund_details = fields.List(fields.Dict(required=False), required=False)
    
    total_refund_amount = fields.Int(required=False)
    


class RefundSourcesPriority(BaseSchema):
    # Payment swagger.json

    
    enabled = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    source = fields.Str(required=False)
    


class RefundPriorityResponseSerializer(BaseSchema):
    # Payment swagger.json

    
    configuration = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    apportion = fields.Boolean(required=False)
    
    business_unit = fields.Str(required=False)
    
    settle_offline = fields.Boolean(required=False)
    
    refund_sources_priority = fields.List(fields.Nested(RefundSourcesPriority, required=False), required=False)
    
    message = fields.Str(required=False)
    


class RefundPriorityRequestSerializer(BaseSchema):
    # Payment swagger.json

    
    settle_offline = fields.Boolean(required=False)
    
    apportion = fields.Boolean(required=False)
    
    refund_sources_priority = fields.List(fields.Nested(RefundSourcesPriority, required=False), required=False)
    


class FromConfig(BaseSchema):
    # Payment swagger.json

    
    device = fields.Str(required=False)
    
    business_unit = fields.Str(required=False)
    


class ToConfig(BaseSchema):
    # Payment swagger.json

    
    device = fields.List(fields.Str(required=False), required=False)
    
    business_unit = fields.Str(required=False)
    


class PlatformPaymentModeCopyConfigRequest(BaseSchema):
    # Payment swagger.json

    
    from_config = fields.Nested(FromConfig, required=False)
    
    to_config = fields.Nested(ToConfig, required=False)
    


class PaymentMethodsMetaOrder(BaseSchema):
    # Payment swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_extra_identifiers = fields.Dict(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    


class PaymentOrderMethods(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False)
    
    payment = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    meta = fields.Nested(PaymentMethodsMetaOrder, required=False)
    
    name = fields.Str(required=False)
    


class PaymentOrderRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentOrderMethods, required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    customer_details = fields.Nested(CustomerDetails, required=False)
    


class CustomerDetails(BaseSchema):
    # Payment swagger.json

    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class PaymentOrderData(BaseSchema):
    # Payment swagger.json

    
    contact = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False, allow_none=True)
    
    amount = fields.Float(required=False, allow_none=True)
    
    customer_id = fields.Str(required=False, allow_none=True)
    
    currency = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    method = fields.Str(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False, allow_none=True)
    
    url = fields.Str(required=False)
    
    encdata = fields.Str(required=False)
    
    checksum = fields.Str(required=False)
    
    mcode = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    payment_mode_identifier = fields.Str(required=False)
    
    bank = fields.Str(required=False, allow_none=True)
    


class PaymentOrderResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    payment_confirm_url = fields.Str(required=False, allow_none=True)
    
    callback_url = fields.Str(required=False, allow_none=True)
    
    status_code = fields.Int(required=False)
    
    order_id = fields.Str(required=False, allow_none=True)
    
    data = fields.Nested(PaymentOrderData, required=False)
    


class AggregatorVersionItemSchema(BaseSchema):
    # Payment swagger.json

    
    is_equal_to = fields.Str(required=False)
    
    is_less_than = fields.Str(required=False)
    
    is_greater_than = fields.Str(required=False)
    


class AggregatorVersionResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AggregatorVersionItemSchema, required=False), required=False)
    


class AggregatorVersionRequestSchema(BaseSchema):
    # Payment swagger.json

    
    is_equal_to = fields.Str(required=False)
    
    is_less_than = fields.Str(required=False)
    
    is_greater_than = fields.Str(required=False)
    


class AggregatorControlRequest(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.Str(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    device = fields.Str(required=False)
    
    version = fields.Nested(AggregatorVersionRequestSchema, required=False)
    


class PaymentModeCustomConfigSchema(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    business_unit = fields.Str(required=False)
    
    custom_config = fields.Nested(PaymentCustomConfigDetailsSchema, required=False)
    


class PaymentCustomConfigDetailsSchema(BaseSchema):
    # Payment swagger.json

    
    customer = fields.Nested(PaymentCustomConfigCustomerSchema, required=False)
    
    payment_mode = fields.Nested(lambda: PaymentCustomConfigDetailsSchema(exclude=('payment_mode')), required=False)
    
    min_order_value = fields.Float(required=False)
    
    available = fields.Boolean(required=False)
    
    pre_order = fields.List(fields.Str(required=False), required=False)
    
    post_order = fields.List(fields.Str(required=False), required=False)
    


class PaymentCustomConfigCustomerSchema(BaseSchema):
    # Payment swagger.json

    
    restriction = fields.Str(required=False)
    
    groups = fields.List(fields.Int(required=False), required=False)
    
    types = fields.List(fields.Str(required=False), required=False)
    


class PaymentCustomConfigModeSchema(BaseSchema):
    # Payment swagger.json

    
    available = fields.Boolean(required=False)
    
    pre_order = fields.List(fields.Str(required=False), required=False)
    
    post_order = fields.List(fields.Str(required=False), required=False)
    


class PaymentCustomConfigDetailsRequestSchema(BaseSchema):
    # Payment swagger.json

    
    customer = fields.Nested(PaymentCustomConfigCustomerRequestSchema, required=False)
    
    payment_mode = fields.Nested(PaymentCustomConfigModeSchema, required=False)
    
    min_order_value = fields.Float(required=False)
    


class PaymentCustomConfigCustomerRequestSchema(BaseSchema):
    # Payment swagger.json

    
    restriction = fields.Str(required=False)
    
    groups = fields.List(fields.Int(required=False), required=False)
    


class PaymentCustomConfigRequestSchema(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.Str(required=False)
    
    items = fields.List(fields.Nested(PaymentCustomConfigDetailsRequestSchema, required=False), required=False)
    


class PaymentCustomConfigResponseSchema(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(PaymentModeCustomConfigSchema, required=False), required=False)
    


class DeleteBeneficiaryRequest(BaseSchema):
    # Payment swagger.json

    
    beneficiary_id = fields.Str(required=False)
    


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
    
    offline_refund_collect_type = fields.List(fields.Str(required=False), required=False)
    


class OfflineRefundOptions(BaseSchema):
    # Payment swagger.json

    
    items = fields.Nested(RefundOptionsDetails, required=False)
    
    payment_modes = fields.List(fields.Str(required=False), required=False)
    
    offline_refund_collect_type = fields.List(fields.Str(required=False), required=False)
    


class RefundOptionResponse(BaseSchema):
    # Payment swagger.json

    
    offline_refund_options = fields.Nested(OfflineRefundOptions, required=False)
    
    success = fields.Boolean(required=False)
    
    refund_options = fields.Nested(RefundOptions, required=False)
    


class SelectedRefundOptionResponse(BaseSchema):
    # Payment swagger.json

    
    transfer_mode = fields.Nested(TransferMode, required=False)
    
    shipment_id = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    beneficiary_details = fields.Dict(required=False)
    


class TransferMode(BaseSchema):
    # Payment swagger.json

    
    mode = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


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
    


class OrderBeneficiaryResponseSchemaV2(BaseSchema):
    # Payment swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    data = fields.Nested(BeneficiaryRefundOptions, required=False)
    
    limit = fields.Nested(RefundOptionsLimit, required=False)
    


class RefundOptionsLimit(BaseSchema):
    # Payment swagger.json

    
    bank = fields.Int(required=False)
    
    wallet = fields.Int(required=False)
    
    upi = fields.Int(required=False)
    


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
    
    vpa = fields.Nested(VPADetails, required=False)
    


class SetDefaultBeneficiaryRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    merchant_shipment_id = fields.Str(required=False)
    


class SetDefaultBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    is_beneficiary_set = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentRefundRequestMeta(BaseSchema):
    # Payment swagger.json

    
    shipment_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    utr = fields.Str(required=False)
    
    notes = fields.Str(required=False, allow_none=True)
    
    billing_employee_code = fields.Str(required=False, allow_none=True)
    


class ShipmentRefundRequest(BaseSchema):
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
    


class ShipmentRefundResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(ShipmentRefundDetail, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    
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
    


class PennyDropValidationResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    
    allow_pennydrop_validation = fields.Boolean(required=False)
    


class UpdatePennyDropValidationRequest(BaseSchema):
    # Payment swagger.json

    
    allow_pennydrop_validation = fields.Boolean(required=False)
    


class AggregatorConfigResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(PaymentOptionItem, required=False), required=False)
    


class PaymentModeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(PaymentMode, required=False), required=False)
    


class PaymentOptionItem(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    integration_type = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    config = fields.List(fields.Str(required=False), required=False)
    
    payment_modes = fields.List(fields.Nested(PaymentMode, required=False), required=False)
    
    payment_mode = fields.List(fields.Nested(PaymentMode, required=False), required=False)
    
    checkout_type = fields.Str(required=False)
    
    country = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Str(required=False)
    
    save_allowed = fields.Boolean(required=False)
    
    extension_id = fields.Str(required=False, allow_none=True)
    


class PaymentMode(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    payment_id = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    sub_payment_mode = fields.List(fields.Nested(SubPaymentMode, required=False), required=False)
    


class SubPaymentMode(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    


class AggregatorCredentialRequest(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    ccavenue = fields.Nested(AggregatorCredential, required=False)
    
    juspay = fields.Nested(AggregatorCredential, required=False)
    
    razorpay = fields.Nested(AggregatorCredential, required=False)
    
    potlee = fields.Nested(AggregatorCredential, required=False)
    
    jio = fields.Nested(AggregatorCredential, required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    


class PatchAggregatorCredentialResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    aggregators = fields.List(fields.Str(required=False), required=False)
    


class AggregatorCredentialResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    display_fields = fields.List(fields.Str(required=False), required=False)
    
    aggregators = fields.List(fields.Nested(AggregatorCredential, required=False), required=False)
    


class AggregatorCredential(BaseSchema):
    # Payment swagger.json

    
    key = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    merchant_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    config_type = fields.Str(required=False)
    
    display = fields.Nested(AggregatorDisplayItem, required=False)
    
    aggregator = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    integration_type = fields.Str(required=False)
    


class AggregatorDisplayItem(BaseSchema):
    # Payment swagger.json

    
    info = fields.List(fields.Str(required=False), required=False)
    
    link = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    review_status = fields.Str(required=False)
    


class GetDeviceResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    items = fields.Nested(BusinessUnitDevice, required=False)
    


class BusinessUnitDevice(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.List(fields.Nested(BusinessUnit, required=False), required=False)
    
    device = fields.List(fields.Nested(Device, required=False), required=False)
    


class BusinessUnit(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class Device(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class AggregatorHistoryResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(HistoryItem, required=False), required=False)
    


class HistoryItem(BaseSchema):
    # Payment swagger.json

    
    created_on = fields.Str(required=False)
    
    updated_on = fields.Str(required=False)
    
    reviewer = fields.Str(required=False)
    
    comments = fields.Str(required=False)
    
    review_status = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    config_type = fields.Str(required=False)
    
    public_token = fields.Str(required=False)
    
    razorpay_account_id = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    webhook_secret = fields.Str(required=False)
    


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
    


class PaymentMethodConfigResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    refund_to = fields.Nested(RefundTo, required=False)
    
    required_session_paths = fields.List(fields.Nested(RequiredSessionPath, required=False), required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMode, required=False), required=False)
    
    checkout_type = fields.List(fields.Nested(CheckoutType, required=False), required=False)
    
    auto_capture = fields.List(fields.Boolean(required=False), required=False)
    
    mode = fields.List(fields.Nested(Mode, required=False), required=False)
    
    country = fields.List(fields.Nested(Country, required=False), required=False)
    
    currency = fields.List(fields.Nested(Currency, required=False), required=False)
    


class RequiredSessionPath(BaseSchema):
    # Payment swagger.json

    
    version = fields.Str(required=False)
    
    paths = fields.List(fields.Nested(SessionItem, required=False), required=False)
    


class SessionItem(BaseSchema):
    # Payment swagger.json

    
    type = fields.Str(required=False)
    
    uri_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    methods = fields.List(fields.Str(required=False), required=False)
    


class PaymentErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(PaymentError, required=False)
    
    success = fields.Boolean(required=False)
    
    error_msg = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class PaymentError(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.List(fields.Str(required=False), required=False)
    
    transaction_amount_in_paise = fields.List(fields.Str(required=False), required=False)
    


class ShipmentBeneficiaryDetailsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    transfer_mode = fields.Nested(TransferMode, required=False)
    
    message = fields.Str(required=False)
    
    beneficiary_details = fields.Str(required=False)
    


