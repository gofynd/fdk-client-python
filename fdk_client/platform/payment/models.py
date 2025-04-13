"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class PaymentGatewayConfigDetails(BaseSchema):
    pass


class ErrorCodeDescription(BaseSchema):
    pass


class PaymentGatewayConfig(BaseSchema):
    pass


class PaymentGatewayConfigCreation(BaseSchema):
    pass


class PaymentGatewayToBeReviewed(BaseSchema):
    pass


class ErrorCodeAndDescription(BaseSchema):
    pass


class HttpErrorDetails(BaseSchema):
    pass


class IntentAppErrorList(BaseSchema):
    pass


class ProductCODData(BaseSchema):
    pass


class CODChargesLimitsDetails(BaseSchema):
    pass


class PaymentModeLogo(BaseSchema):
    pass


class IntentApp(BaseSchema):
    pass


class PaymentModeList(BaseSchema):
    pass


class RootPaymentMode(BaseSchema):
    pass


class PaymentOptions(BaseSchema):
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


class PaymentOptionsDetails(BaseSchema):
    pass


class PayoutCustomer(BaseSchema):
    pass


class PayoutMoreAttributes(BaseSchema):
    pass


class PayoutAggregator(BaseSchema):
    pass


class Payout(BaseSchema):
    pass


class PayoutsDetails(BaseSchema):
    pass


class PayoutBankDetails(BaseSchema):
    pass


class PayoutCreation(BaseSchema):
    pass


class PayoutDetails(BaseSchema):
    pass


class UpdatePayoutDetails(BaseSchema):
    pass


class UpdatePayoutCreation(BaseSchema):
    pass


class DeletePayoutDetails(BaseSchema):
    pass


class SubscriptionPaymentMethodDetails(BaseSchema):
    pass


class DeleteSubscriptionPaymentMethodDetails(BaseSchema):
    pass


class SubscriptionConfigDetails(BaseSchema):
    pass


class SaveSubscriptionSetupIntentCreation(BaseSchema):
    pass


class SaveSubscriptionSetupIntentDetails(BaseSchema):
    pass


class RefundAccountDetails(BaseSchema):
    pass


class NotFoundResourceError(BaseSchema):
    pass


class BankDetailsForOTP(BaseSchema):
    pass


class AddBeneficiaryDetailsOTPCreation(BaseSchema):
    pass


class IfscCodeDetails(BaseSchema):
    pass


class OrderBeneficiaryDetails(BaseSchema):
    pass


class OrderBeneficiaryFetchResults(BaseSchema):
    pass


class MultiTenderPaymentMeta(BaseSchema):
    pass


class MultiTenderPaymentMethod(BaseSchema):
    pass


class PaymentConfirmationCreation(BaseSchema):
    pass


class PaymentConfirmationDetails(BaseSchema):
    pass


class CODdata(BaseSchema):
    pass


class CODLimitConfig(BaseSchema):
    pass


class CODPaymentLimitConfig(BaseSchema):
    pass


class GetUserBULimitResponseSchema(BaseSchema):
    pass


class GetUserCODLimitDetails(BaseSchema):
    pass


class SetCODForUserCreation(BaseSchema):
    pass


class SetCODOptionDetails(BaseSchema):
    pass


class EdcModelData(BaseSchema):
    pass


class EdcAggregatorAndModelListDetails(BaseSchema):
    pass


class StatisticsData(BaseSchema):
    pass


class EdcDeviceStatsDetails(BaseSchema):
    pass


class EdcAddCreation(BaseSchema):
    pass


class EdcDevice(BaseSchema):
    pass


class EdcDeviceAddDetails(BaseSchema):
    pass


class EdcDeviceDetails(BaseSchema):
    pass


class EdcUpdate(BaseSchema):
    pass


class EdcDeviceUpdateDetails(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class EdcDeviceListDetails(BaseSchema):
    pass


class PaymentInitializationCreation(BaseSchema):
    pass


class PaymentInitializationDetails(BaseSchema):
    pass


class PaymentStatusUpdateCreation(BaseSchema):
    pass


class PaymentStatusUpdateDetails(BaseSchema):
    pass


class ResendOrCancelPaymentCreation(BaseSchema):
    pass


class LinkStatus(BaseSchema):
    pass


class ResendOrCancelPaymentDetails(BaseSchema):
    pass


class PaymentStatusBulkHandlerCreation(BaseSchema):
    pass


class PaymentObjectList(BaseSchema):
    pass


class PaymentStatusObject(BaseSchema):
    pass


class PaymentStatusBulkHandlerDetails(BaseSchema):
    pass


class GetOauthUrlDetails(BaseSchema):
    pass


class RevokeOAuthToken(BaseSchema):
    pass


class RepaymentRequestDetails(BaseSchema):
    pass


class RepaymentDetailsSerialiserPayAll(BaseSchema):
    pass


class RepaymentDetails(BaseSchema):
    pass


class MerchantOnBoardingCreation(BaseSchema):
    pass


class MerchantOnBoardingDetails(BaseSchema):
    pass


class ValidateCustomerCreation(BaseSchema):
    pass


class ValidateCustomerDetails(BaseSchema):
    pass


class GetPaymentLinkDetails(BaseSchema):
    pass


class ErrorDescription(BaseSchema):
    pass


class ErrorDetails(BaseSchema):
    pass


class CreatePaymentLinkMeta(BaseSchema):
    pass


class CreatePaymentLinkCreation(BaseSchema):
    pass


class CreatePaymentLinkDetails(BaseSchema):
    pass


class PollingPaymentLinkDetails(BaseSchema):
    pass


class CancelOrResendPaymentLinkCreation(BaseSchema):
    pass


class ResendPaymentLinkDetails(BaseSchema):
    pass


class CancelPaymentLinkDetails(BaseSchema):
    pass


class Code(BaseSchema):
    pass


class PaymentCode(BaseSchema):
    pass


class GetPaymentCode(BaseSchema):
    pass


class GetPaymentCodeDetails(BaseSchema):
    pass


class PlatformPaymentModeDetails(BaseSchema):
    pass


class MerchnatPaymentModeCreation(BaseSchema):
    pass


class OrderDetail(BaseSchema):
    pass


class AddressDetail(BaseSchema):
    pass


class PaymentSessionDetail(BaseSchema):
    pass


class PaymentSessionCreation(BaseSchema):
    pass


class PaymentSessionPutDetails(BaseSchema):
    pass


class RefundSessionDetail(BaseSchema):
    pass


class RefundSessionCreation(BaseSchema):
    pass


class RefundSessionDetails(BaseSchema):
    pass


class PaymentDetails(BaseSchema):
    pass


class CartDetails(BaseSchema):
    pass


class RefundDetails(BaseSchema):
    pass


class PaymentSessionFetchDetails(BaseSchema):
    pass


class RefundSourcesPriority(BaseSchema):
    pass


class RefundPriorityDetails(BaseSchema):
    pass


class RefundPriorityCreation(BaseSchema):
    pass


class MerchantPaymentModeCreation(BaseSchema):
    pass


class FromConfig(BaseSchema):
    pass


class ToConfig(BaseSchema):
    pass


class PlatformPaymentModeCopyConfigCreation(BaseSchema):
    pass


class PaymentMethodsMetaOrder(BaseSchema):
    pass


class PaymentOrderMethods(BaseSchema):
    pass


class PaymentOrderCreation(BaseSchema):
    pass


class PaymentOrderData(BaseSchema):
    pass


class PaymentOrderDetails(BaseSchema):
    pass


class AggregatorVersionItemSchema(BaseSchema):
    pass


class AggregatorVersionDetails(BaseSchema):
    pass


class AggregatorVersionRequestSchema(BaseSchema):
    pass


class PatchAggregatorControl(BaseSchema):
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





class PaymentGatewayConfigDetails(BaseSchema):
    # Payment swagger.json

    
    aggregators = fields.List(fields.Dict(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    
    display_fields = fields.List(fields.Str(required=False), required=False)
    


class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentGatewayConfig(BaseSchema):
    # Payment swagger.json

    
    secret = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    key = fields.Str(required=False)
    
    merchant_salt = fields.Str(required=False)
    


class PaymentGatewayConfigCreation(BaseSchema):
    # Payment swagger.json

    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False, allow_none=True)
    
    aggregator_name = fields.Nested(PaymentGatewayConfig, required=False)
    


class PaymentGatewayToBeReviewed(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class HttpErrorDetails(BaseSchema):
    # Payment swagger.json

    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    
    success = fields.Boolean(required=False)
    


class IntentAppErrorList(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False, allow_none=True)
    


class ProductCODData(BaseSchema):
    # Payment swagger.json

    
    items = fields.Dict(required=False, allow_none=True)
    
    cod_charges = fields.Nested(CODChargesLimitsDetails, required=False)
    


class CODChargesLimitsDetails(BaseSchema):
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
    
    aggregator_name = fields.Str(required=False, allow_none=True)
    


class PaymentOptions(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    


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
    


class PaymentOptionAndFlow(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    
    payment_default_selection = fields.Nested(PaymentDefaultSelection, required=False)
    


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
    


class PaymentOptionsDetails(BaseSchema):
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
    


class PayoutsDetails(BaseSchema):
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
    


class PayoutCreation(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    users = fields.Dict(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    transfer_type = fields.Str(required=False)
    


class PayoutDetails(BaseSchema):
    # Payment swagger.json

    
    payment_status = fields.Str(required=False)
    
    users = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    unique_transfer_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    bank_details = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    created = fields.Boolean(required=False)
    
    payouts = fields.Dict(required=False)
    


class UpdatePayoutDetails(BaseSchema):
    # Payment swagger.json

    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class UpdatePayoutCreation(BaseSchema):
    # Payment swagger.json

    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    unique_external_id = fields.Str(required=False)
    


class DeletePayoutDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    


class SubscriptionPaymentMethodDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class DeleteSubscriptionPaymentMethodDetails(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    


class SubscriptionConfigDetails(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    config = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class SaveSubscriptionSetupIntentCreation(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False)
    


class SaveSubscriptionSetupIntentDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class RefundAccountDetails(BaseSchema):
    # Payment swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
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
    


class AddBeneficiaryDetailsOTPCreation(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    


class IfscCodeDetails(BaseSchema):
    # Payment swagger.json

    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
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
    
    account_no = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class OrderBeneficiaryFetchResults(BaseSchema):
    # Payment swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Payment swagger.json

    
    extra_meta = fields.Dict(required=False, allow_none=True)
    
    order_id = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    payment_gateway_slug = fields.Str(required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    amount = fields.Float(required=False)
    
    mode = fields.Str(required=False)
    


class PaymentConfirmationCreation(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    


class PaymentConfirmationDetails(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CODdata(BaseSchema):
    # Payment swagger.json

    
    remaining_limit = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    
    usages = fields.Int(required=False)
    


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
    


class GetUserBULimitResponseSchema(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    config = fields.Nested(CODPaymentLimitConfig, required=False)
    


class GetUserCODLimitDetails(BaseSchema):
    # Payment swagger.json

    
    items = fields.List(fields.Nested(GetUserBULimitResponseSchema, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class SetCODForUserCreation(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.Str(required=False)
    
    mobileno = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    merchant_user_id = fields.Str(required=False)
    


class SetCODOptionDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class EdcModelData(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    models = fields.List(fields.Str(required=False), required=False)
    


class EdcAggregatorAndModelListDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(EdcModelData, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class StatisticsData(BaseSchema):
    # Payment swagger.json

    
    inactive_device_count = fields.Int(required=False)
    
    active_device_count = fields.Int(required=False)
    


class EdcDeviceStatsDetails(BaseSchema):
    # Payment swagger.json

    
    statistics = fields.Nested(StatisticsData, required=False)
    
    success = fields.Boolean(required=False)
    


class EdcAddCreation(BaseSchema):
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
    


class EdcDeviceAddDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EdcDevice, required=False)
    
    success = fields.Boolean(required=False)
    


class EdcDeviceDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(EdcDevice, required=False)
    
    success = fields.Boolean(required=False)
    


class EdcUpdate(BaseSchema):
    # Payment swagger.json

    
    edc_model = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    merchant_store_pos_code = fields.Str(required=False)
    
    device_tag = fields.Str(required=False, allow_none=True)
    


class EdcDeviceUpdateDetails(BaseSchema):
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
    


class EdcDeviceListDetails(BaseSchema):
    # Payment swagger.json

    
    items = fields.List(fields.Nested(EdcDevice, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    


class PaymentInitializationCreation(BaseSchema):
    # Payment swagger.json

    
    razorpay_payment_id = fields.Str(required=False, allow_none=True)
    
    device_id = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False, allow_none=True)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    contact = fields.Str(required=False)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    merchant_order_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    


class PaymentInitializationDetails(BaseSchema):
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
    
    amount = fields.Int(required=False, allow_none=True)
    
    timeout = fields.Int(required=False, allow_none=True)
    
    virtual_id = fields.Str(required=False, allow_none=True)
    
    bqr_image = fields.Str(required=False, allow_none=True)
    
    aggregator_order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    method = fields.Str(required=False)
    


class PaymentStatusUpdateCreation(BaseSchema):
    # Payment swagger.json

    
    device_id = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    contact = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    


class PaymentStatusUpdateDetails(BaseSchema):
    # Payment swagger.json

    
    redirect_url = fields.Str(required=False, allow_none=True)
    
    retry = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False, allow_none=True)
    
    status = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    


class ResendOrCancelPaymentCreation(BaseSchema):
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
    


class PaymentStatusBulkHandlerCreation(BaseSchema):
    # Payment swagger.json

    
    merchant_order_id = fields.List(fields.Str(required=False), required=False)
    


class PaymentObjectList(BaseSchema):
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
    
    payment_object_list = fields.List(fields.Nested(PaymentObjectList, required=False), required=False)
    


class PaymentStatusBulkHandlerDetails(BaseSchema):
    # Payment swagger.json

    
    count = fields.Int(required=False)
    
    data = fields.List(fields.Nested(PaymentStatusObject, required=False), required=False)
    
    success = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
    status = fields.Int(required=False)
    


class GetOauthUrlDetails(BaseSchema):
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
    
    extension_order_id = fields.Str(required=False)
    
    aggregator_transaction_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    shipment_details = fields.List(fields.Nested(RepaymentRequestDetails, required=False), required=False)
    


class RepaymentDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class MerchantOnBoardingCreation(BaseSchema):
    # Payment swagger.json

    
    credit_line_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class MerchantOnBoardingDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class ValidateCustomerCreation(BaseSchema):
    # Payment swagger.json

    
    phone_number = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    payload = fields.Str(required=False, allow_none=True)
    
    delivery_address = fields.Dict(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    order_items = fields.List(fields.Dict(required=False), required=False)
    
    merchant_params = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    


class ValidateCustomerDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


class GetPaymentLinkDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    amount = fields.Float(required=False, allow_none=True)
    
    merchant_name = fields.Str(required=False, allow_none=True)
    
    payment_link_url = fields.Str(required=False, allow_none=True)
    
    payment_link_current_status = fields.Str(required=False, allow_none=True)
    
    external_order_id = fields.Str(required=False, allow_none=True)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    


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
    
    amount = fields.Str(required=False)
    
    assign_card_id = fields.Str(required=False, allow_none=True)
    


class CreatePaymentLinkCreation(BaseSchema):
    # Payment swagger.json

    
    email = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    mobile_number = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    description = fields.Str(required=False, allow_none=True)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    
    external_order_id = fields.Str(required=False)
    
    success_redirection_url = fields.Str(required=False)
    
    failure_redirection_url = fields.Str(required=False)
    


class CreatePaymentLinkDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    payment_link_url = fields.Str(required=False, allow_none=True)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    
    payment_link_id = fields.Str(required=False, allow_none=True)
    


class PollingPaymentLinkDetails(BaseSchema):
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
    


class CancelOrResendPaymentLinkCreation(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    


class ResendPaymentLinkDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    polling_timeout = fields.Int(required=False, allow_none=True)
    
    success = fields.Boolean(required=False)
    


class CancelPaymentLinkDetails(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class Code(BaseSchema):
    # Payment swagger.json

    
    name = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class PaymentCode(BaseSchema):
    # Payment swagger.json

    
    networks = fields.Str(required=False)
    
    codes = fields.Nested(Code, required=False)
    
    name = fields.Str(required=False)
    
    types = fields.Str(required=False)
    


class GetPaymentCode(BaseSchema):
    # Payment swagger.json

    
    method_code = fields.Nested(PaymentCode, required=False)
    


class GetPaymentCodeDetails(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(GetPaymentCode, required=False)
    
    success = fields.Boolean(required=False)
    


class PlatformPaymentModeDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class MerchnatPaymentModeCreation(BaseSchema):
    # Payment swagger.json

    
    offline = fields.Dict(required=False, allow_none=True)
    
    online = fields.Dict(required=False, allow_none=True)
    


class OrderDetail(BaseSchema):
    # Payment swagger.json

    
    gid = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    aggregator_order_details = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    


class AddressDetail(BaseSchema):
    # Payment swagger.json

    
    google_map_point = fields.Dict(required=False)
    
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
    
    payment_methods = fields.List(fields.Dict(required=False), required=False)
    
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
    


class PaymentSessionCreation(BaseSchema):
    # Payment swagger.json

    
    meta = fields.Dict(required=False)
    
    gid = fields.Str(required=False)
    
    order_details = fields.Nested(OrderDetail, required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    payment_details = fields.List(fields.Nested(PaymentSessionDetail, required=False), required=False)
    
    total_amount = fields.Int(required=False)
    
    checksum = fields.Str(required=False)
    
    source = fields.Str(required=False)
    


class PaymentSessionPutDetails(BaseSchema):
    # Payment swagger.json

    
    gid = fields.Str(required=False)
    
    platform_transaction_details = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    total_amount = fields.Int(required=False)
    


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
    
    receipt_number = fields.Str(required=False)
    
    pg_refund_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    transfer_reversal = fields.Str(required=False)
    
    balance_transaction = fields.Str(required=False)
    


class RefundSessionCreation(BaseSchema):
    # Payment swagger.json

    
    meta = fields.Dict(required=False)
    
    gid = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    payment_details = fields.Nested(PaymentSessionDetail, required=False)
    
    total_amount = fields.Int(required=False)
    
    refund_details = fields.List(fields.Nested(RefundSessionDetail, required=False), required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    
    message = fields.Str(required=False)
    
    checksum = fields.Str(required=False)
    


class RefundSessionDetails(BaseSchema):
    # Payment swagger.json

    
    gid = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    platform_refund_details = fields.List(fields.Dict(required=False), required=False)
    
    total_refund_amount = fields.Int(required=False)
    


class PaymentDetails(BaseSchema):
    # Payment swagger.json

    
    payment_methods = fields.List(fields.Dict(required=False), required=False)
    
    gid = fields.Str(required=False)
    
    amount_refunded = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    merchant_locale = fields.Str(required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    kind = fields.Str(required=False)
    
    success_url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    captured = fields.Boolean(required=False)
    
    payment_id = fields.Str(required=False)
    
    g_user_id = fields.Str(required=False)
    
    locale = fields.Str(required=False)
    
    cancel_url = fields.Str(required=False)
    
    created = fields.Str(required=False)
    
    amount_captured = fields.Int(required=False)
    
    amount = fields.Int(required=False)
    
    aggregator_customer_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    


class CartDetails(BaseSchema):
    # Payment swagger.json

    
    items = fields.Dict(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    cart_value = fields.Float(required=False)
    
    total_quantity = fields.Int(required=False)
    
    custom_cart_meta = fields.Dict(required=False)
    


class RefundDetails(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    created = fields.Str(required=False)
    
    refund_utr = fields.Str(required=False)
    


class PaymentSessionFetchDetails(BaseSchema):
    # Payment swagger.json

    
    payment_details = fields.Raw(required=False)
    
    currency = fields.Str(required=False, allow_none=True)
    
    status = fields.Str(required=False)
    
    total_amount = fields.Int(required=False)
    
    gid = fields.Str(required=False)
    
    cart_details = fields.Nested(CartDetails, required=False)
    
    refund_details = fields.List(fields.Nested(RefundDetails, required=False), required=False)
    


class RefundSourcesPriority(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    source = fields.Str(required=False)
    


class RefundPriorityDetails(BaseSchema):
    # Payment swagger.json

    
    configuration = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    apportion = fields.Boolean(required=False)
    
    refund_sources_priority = fields.List(fields.Nested(RefundSourcesPriority, required=False), required=False)
    
    message = fields.Str(required=False)
    


class RefundPriorityCreation(BaseSchema):
    # Payment swagger.json

    
    apportion = fields.Boolean(required=False)
    
    refund_sources_priority = fields.List(fields.Nested(RefundSourcesPriority, required=False), required=False)
    


class MerchantPaymentModeCreation(BaseSchema):
    # Payment swagger.json

    
    business_unit = fields.Str(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    device = fields.Dict(required=False)
    


class FromConfig(BaseSchema):
    # Payment swagger.json

    
    device = fields.Str(required=False)
    
    business_unit = fields.Str(required=False)
    


class ToConfig(BaseSchema):
    # Payment swagger.json

    
    device = fields.List(fields.Dict(required=False), required=False)
    
    business_unit = fields.Str(required=False)
    


class PlatformPaymentModeCopyConfigCreation(BaseSchema):
    # Payment swagger.json

    
    from_config = fields.Nested(FromConfig, required=False)
    
    to_config = fields.Nested(ToConfig, required=False)
    


class PaymentMethodsMetaOrder(BaseSchema):
    # Payment swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    


class PaymentOrderMethods(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False)
    
    payment = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    meta = fields.Nested(PaymentMethodsMetaOrder, required=False)
    
    name = fields.Str(required=False)
    


class PaymentOrderCreation(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentOrderMethods, required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    


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
    


class PaymentOrderDetails(BaseSchema):
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
    


class AggregatorVersionDetails(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    items = fields.Nested(AggregatorVersionItemSchema, required=False)
    


class AggregatorVersionRequestSchema(BaseSchema):
    # Payment swagger.json

    
    is_equal_to = fields.Str(required=False)
    
    is_less_than = fields.Str(required=False)
    
    is_greater_than = fields.Str(required=False)
    


class PatchAggregatorControl(BaseSchema):
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
    
    payment_mode = fields.Nested(PaymentCustomConfigModeSchema, required=False)
    
    min_order_value = fields.Float(required=False)
    


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
    


