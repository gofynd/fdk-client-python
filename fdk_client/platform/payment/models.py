"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class PaymentGatewayConfigResponse(BaseSchema):
    pass


class ErrorCodeDescription(BaseSchema):
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


class PaymentOptions(BaseSchema):
    pass


class PaymentOptionsResponse(BaseSchema):
    pass


class PayoutAggregator(BaseSchema):
    pass


class PayoutMoreAttributes(BaseSchema):
    pass


class PayoutCustomer(BaseSchema):
    pass


class Payout(BaseSchema):
    pass


class PayoutsResponse(BaseSchema):
    pass


class PayoutBankDetails(BaseSchema):
    pass


class PayoutRequest(BaseSchema):
    pass


class PayoutResponse(BaseSchema):
    pass


class UpdatePayoutResponse(BaseSchema):
    pass


class UpdatePayoutRequest(BaseSchema):
    pass


class DeletePayoutResponse(BaseSchema):
    pass


class SubscriptionPaymentMethodResponse(BaseSchema):
    pass


class DeleteSubscriptionPaymentMethodResponse(BaseSchema):
    pass


class SubscriptionConfigResponse(BaseSchema):
    pass


class SaveSubscriptionSetupIntentRequest(BaseSchema):
    pass


class SaveSubscriptionSetupIntentResponse(BaseSchema):
    pass


class RefundAccountResponse(BaseSchema):
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


class PlatformPaymentOptions(BaseSchema):
    pass


class PlatfromPaymentConfig(BaseSchema):
    pass


class UpdatePlatformPaymentConfig(BaseSchema):
    pass


class CODdata(BaseSchema):
    pass


class GetUserCODLimitResponse(BaseSchema):
    pass


class SetCODForUserRequest(BaseSchema):
    pass


class SetCODOptionResponse(BaseSchema):
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


class ValidateCustomerRequest(BaseSchema):
    pass


class ValidateCustomerResponse(BaseSchema):
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


class CancelPaymentLinkResponse(BaseSchema):
    pass





class PaymentGatewayConfigResponse(BaseSchema):
    # Payment swagger.json

    
    display_fields = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    aggregators = fields.List(fields.Dict(required=False), required=False)
    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    


class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class PaymentGatewayConfig(BaseSchema):
    # Payment swagger.json

    
    merchant_salt = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PaymentGatewayConfigRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator_name = fields.Nested(PaymentGatewayConfig, required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PaymentGatewayToBeReviewed(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    aggregator = fields.List(fields.Str(required=False), required=False)
    


class ErrorCodeAndDescription(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class HttpErrorCodeAndResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    


class PaymentModeLogo(BaseSchema):
    # Payment swagger.json

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    


class IntentApp(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    code = fields.Str(required=False)
    


class IntentAppErrorList(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    cod_limit_per_order = fields.Float(required=False)
    
    exp_year = fields.Int(required=False)
    
    card_type = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    card_reference = fields.Str(required=False)
    
    card_isin = fields.Str(required=False)
    
    exp_month = fields.Int(required=False)
    
    intent_app = fields.List(fields.Nested(IntentApp, required=False), required=False)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    
    card_brand_image = fields.Str(required=False)
    
    cod_limit = fields.Float(required=False)
    
    remaining_limit = fields.Float(required=False)
    
    card_name = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    nickname = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    card_issuer = fields.Str(required=False)
    
    compliant_with_tokenisation_guidelines = fields.Boolean(required=False)
    
    intent_app_error_dict_list = fields.List(fields.Nested(IntentAppErrorList, required=False), required=False)
    
    display_priority = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    intent_flow = fields.Boolean(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    fynd_vpa = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    retry_count = fields.Int(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    card_brand = fields.Str(required=False)
    
    card_number = fields.Str(required=False)
    


class RootPaymentMode(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    is_pay_by_card_pl = fields.Boolean(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    
    aggregator_name = fields.Str(required=False)
    
    save_card = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    display_priority = fields.Int(required=False)
    


class PaymentOptions(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    


class PaymentOptionsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    payment_options = fields.Nested(PaymentOptions, required=False)
    


class PayoutAggregator(BaseSchema):
    # Payment swagger.json

    
    payout_details_id = fields.Int(required=False)
    
    aggregator_fund_id = fields.Int(required=False)
    
    aggregator_id = fields.Int(required=False)
    


class PayoutMoreAttributes(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    


class PayoutCustomer(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    mobile = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class Payout(BaseSchema):
    # Payment swagger.json

    
    unique_transfer_no = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    payouts_aggregators = fields.List(fields.Nested(PayoutAggregator, required=False), required=False)
    
    transfer_type = fields.Str(required=False)
    
    more_attributes = fields.Nested(PayoutMoreAttributes, required=False)
    
    customers = fields.Nested(PayoutCustomer, required=False)
    
    is_active = fields.Boolean(required=False)
    


class PayoutsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(Payout, required=False), required=False)
    


class PayoutBankDetails(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    account_holder = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    


class PayoutRequest(BaseSchema):
    # Payment swagger.json

    
    users = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    transfer_type = fields.Str(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    is_active = fields.Boolean(required=False)
    


class PayoutResponse(BaseSchema):
    # Payment swagger.json

    
    unique_transfer_no = fields.Str(required=False)
    
    users = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    transfer_type = fields.Str(required=False)
    
    payouts = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    
    bank_details = fields.Dict(required=False)
    
    payment_status = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class UpdatePayoutResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    


class UpdatePayoutRequest(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    unique_external_id = fields.Str(required=False)
    


class DeletePayoutResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    


class SubscriptionPaymentMethodResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    


class DeleteSubscriptionPaymentMethodResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    


class SubscriptionConfigResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    config = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    


class SaveSubscriptionSetupIntentRequest(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False)
    


class SaveSubscriptionSetupIntentResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    


class RefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    


class NotFoundResourceError(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class BankDetailsForOTP(BaseSchema):
    # Payment swagger.json

    
    account_no = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    


class AddBeneficiaryDetailsOTPRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    details = fields.Nested(BankDetailsForOTP, required=False)
    


class IfscCodeResponse(BaseSchema):
    # Payment swagger.json

    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    bank_name = fields.Str(required=False)
    


class OrderBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    id = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    


class OrderBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    


class MultiTenderPaymentMeta(BaseSchema):
    # Payment swagger.json

    
    current_status = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    


class MultiTenderPaymentMethod(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
    name = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    


class PaymentConfirmationRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    


class PaymentConfirmationResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class PlatformPaymentOptions(BaseSchema):
    # Payment swagger.json

    
    enabled = fields.Boolean(required=False)
    
    callback_url = fields.Dict(required=False)
    
    anonymous_cod = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Dict(required=False)
    
    cod_charges = fields.Int(required=False)
    
    source = fields.Str(required=False)
    
    methods = fields.Dict(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    cod_amount_limit = fields.Int(required=False)
    


class PlatfromPaymentConfig(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Nested(PlatformPaymentOptions, required=False)
    


class UpdatePlatformPaymentConfig(BaseSchema):
    # Payment swagger.json

    
    anonymous_cod = fields.Boolean(required=False)
    
    cod_charges = fields.Int(required=False)
    
    payment_selection_lock = fields.Dict(required=False)
    
    methods = fields.Dict(required=False)
    
    cod_amount_limit = fields.Int(required=False)
    


class CODdata(BaseSchema):
    # Payment swagger.json

    
    remaining_limit = fields.Int(required=False)
    
    usages = fields.Int(required=False)
    
    limit = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    


class GetUserCODLimitResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    user_cod_data = fields.Nested(CODdata, required=False)
    


class SetCODForUserRequest(BaseSchema):
    # Payment swagger.json

    
    merchant_user_id = fields.Str(required=False)
    
    mobileno = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class SetCODOptionResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class EdcModelData(BaseSchema):
    # Payment swagger.json

    
    models = fields.List(fields.Str(required=False), required=False)
    
    aggregator = fields.Str(required=False)
    
    aggregator_id = fields.Int(required=False)
    


class EdcAggregatorAndModelListResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(EdcModelData, required=False), required=False)
    


class StatisticsData(BaseSchema):
    # Payment swagger.json

    
    inactive_device_count = fields.Int(required=False)
    
    active_device_count = fields.Int(required=False)
    


class EdcDeviceStatsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    statistics = fields.Nested(StatisticsData, required=False)
    


class EdcAddRequest(BaseSchema):
    # Payment swagger.json

    
    edc_model = fields.Str(required=False)
    
    device_tag = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    terminal_serial_no = fields.Str(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    


class EdcDevice(BaseSchema):
    # Payment swagger.json

    
    edc_model = fields.Str(required=False)
    
    terminal_unique_identifier = fields.Str(required=False)
    
    device_tag = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    terminal_serial_no = fields.Str(required=False)
    
    merchant_store_pos_code = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class EdcDeviceAddResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(EdcDevice, required=False)
    


class EdcDeviceDetailsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(EdcDevice, required=False)
    


class EdcUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    edc_model = fields.Str(required=False)
    
    device_tag = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    merchant_store_pos_code = fields.Str(required=False)
    
    aggregator_id = fields.Int(required=False)
    
    edc_device_serial_no = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


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
    


class EdcDeviceListResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(EdcDevice, required=False), required=False)
    


class PaymentInitializationRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    device_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    customer_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    


class PaymentInitializationResponse(BaseSchema):
    # Payment swagger.json

    
    method = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    upi_poll_url = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    amount = fields.Int(required=False)
    
    order_id = fields.Str(required=False)
    
    polling_url = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    bqr_image = fields.Str(required=False)
    
    device_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    virtual_id = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    vpa = fields.Str(required=False)
    


class PaymentStatusUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    merchant_transaction_id = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    device_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    


class PaymentStatusUpdateResponse(BaseSchema):
    # Payment swagger.json

    
    aggregator_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    retry = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    redirect_url = fields.Str(required=False)
    


class ResendOrCancelPaymentRequest(BaseSchema):
    # Payment swagger.json

    
    request_type = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    device_id = fields.Str(required=False)
    


class LinkStatus(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    


class ResendOrCancelPaymentResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(LinkStatus, required=False)
    


class PaymentStatusBulkHandlerRequest(BaseSchema):
    # Payment swagger.json

    
    merchant_order_id = fields.List(fields.Str(required=False), required=False)
    


class PaymentObjectListSerializer(BaseSchema):
    # Payment swagger.json

    
    created_on = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    refunded_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    amount_in_paisa = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    user_object = fields.Dict(required=False)
    
    application_id = fields.Str(required=False)
    
    refund_object = fields.Dict(required=False)
    
    payment_id = fields.Str(required=False)
    
    aggregator_payment_object = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    all_status = fields.List(fields.Str(required=False), required=False)
    
    collected_by = fields.Str(required=False)
    
    payment_mode_identifier = fields.Str(required=False)
    


class PaymentStatusObject(BaseSchema):
    # Payment swagger.json

    
    payment_object_list = fields.List(fields.Nested(PaymentObjectListSerializer, required=False), required=False)
    
    merchant_order_id = fields.Str(required=False)
    


class PaymentStatusBulkHandlerResponse(BaseSchema):
    # Payment swagger.json

    
    error = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    status = fields.Int(required=False)
    
    success = fields.Str(required=False)
    
    data = fields.List(fields.Nested(PaymentStatusObject, required=False), required=False)
    


class GetOauthUrlResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    


class RevokeOAuthToken(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    delivery_address = fields.Dict(required=False)
    
    payload = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    order_items = fields.List(fields.Dict(required=False), required=False)
    
    merchant_params = fields.Dict(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    phone_number = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    


class ValidateCustomerResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    error = fields.Dict(required=False)
    


class GetPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    merchant_name = fields.Str(required=False)
    
    external_order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    polling_timeout = fields.Int(required=False)
    
    amount = fields.Float(required=False)
    
    payment_link_url = fields.Str(required=False)
    
    payment_link_current_status = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class ErrorDescription(BaseSchema):
    # Payment swagger.json

    
    merchant_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    invalid_id = fields.Boolean(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    
    cancelled = fields.Boolean(required=False)
    
    payment_transaction_id = fields.Str(required=False)
    
    msg = fields.Str(required=False)
    


class ErrorResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    error = fields.Nested(ErrorDescription, required=False)
    


class CreatePaymentLinkMeta(BaseSchema):
    # Payment swagger.json

    
    pincode = fields.Str(required=False)
    
    assign_card_id = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    


class CreatePaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    external_order_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    email = fields.Str(required=False)
    
    mobile_number = fields.Str(required=False)
    
    meta = fields.Nested(CreatePaymentLinkMeta, required=False)
    


class CreatePaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    polling_timeout = fields.Int(required=False)
    
    payment_link_url = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PollingPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    status_code = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    http_status = fields.Int(required=False)
    
    redirect_url = fields.Str(required=False)
    


class CancelOrResendPaymentLinkRequest(BaseSchema):
    # Payment swagger.json

    
    payment_link_id = fields.Str(required=False)
    


class ResendPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    polling_timeout = fields.Int(required=False)
    


class CancelPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


