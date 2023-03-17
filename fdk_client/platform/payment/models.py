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


class IntentAppErrorList(BaseSchema):
    pass


class IntentApp(BaseSchema):
    pass


class PaymentModeList(BaseSchema):
    pass


class RootPaymentMode(BaseSchema):
    pass


class PaymentOptions(BaseSchema):
    pass


class PaymentOptionsResponse(BaseSchema):
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


class BeneficiaryModeDetails(BaseSchema):
    pass


class AddBeneficiaryDetailsRequest(BaseSchema):
    pass


class RefundAccountResponse(BaseSchema):
    pass


class NotFoundResourceError(BaseSchema):
    pass


class IfscCodeResponse(BaseSchema):
    pass


class OrderBeneficiaryDetails(BaseSchema):
    pass


class OrderBeneficiaryResponse(BaseSchema):
    pass


class PaymentConfirmationMode(BaseSchema):
    pass


class PaymentConfirmationRequest(BaseSchema):
    pass


class PaymentConfirmationResponse(BaseSchema):
    pass


class CODdata(BaseSchema):
    pass


class GetUserCODLimitResponse(BaseSchema):
    pass


class SetCODForUserRequest(BaseSchema):
    pass


class SetCODOptionResponse(BaseSchema):
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





class PaymentGatewayConfigResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    display_fields = fields.List(fields.Str(required=False), required=False)
    
    aggregators = fields.List(fields.Dict(required=False), required=False)
    
    created = fields.Boolean(required=False)
    
    excluded_fields = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    


class ErrorCodeDescription(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class PaymentGatewayConfig(BaseSchema):
    # Payment swagger.json

    
    key = fields.Str(required=False)
    
    merchant_salt = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PaymentGatewayConfigRequest(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    aggregator_name = fields.Nested(PaymentGatewayConfig, required=False)
    


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
    


class IntentAppErrorList(BaseSchema):
    # Payment swagger.json

    
    package_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class IntentApp(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    package_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class PaymentModeList(BaseSchema):
    # Payment swagger.json

    
    card_brand = fields.Str(required=False)
    
    card_name = fields.Str(required=False)
    
    exp_month = fields.Int(required=False)
    
    exp_year = fields.Int(required=False)
    
    nickname = fields.Str(required=False)
    
    fynd_vpa = fields.Str(required=False)
    
    card_number = fields.Str(required=False)
    
    card_isin = fields.Str(required=False)
    
    card_type = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    cod_limit = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    card_id = fields.Str(required=False)
    
    logo_url = fields.Nested(PaymentModeLogo, required=False)
    
    display_name = fields.Str(required=False)
    
    retry_count = fields.Int(required=False)
    
    intent_app_error_dict_list = fields.List(fields.Nested(IntentAppErrorList, required=False), required=False)
    
    card_reference = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    intent_app = fields.List(fields.Nested(IntentApp, required=False), required=False)
    
    intent_app_error_list = fields.List(fields.Str(required=False), required=False)
    
    remaining_limit = fields.Float(required=False)
    
    intent_flow = fields.Boolean(required=False)
    
    card_issuer = fields.Str(required=False)
    
    card_brand_image = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    card_token = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    cod_limit_per_order = fields.Float(required=False)
    
    card_fingerprint = fields.Str(required=False)
    
    expired = fields.Boolean(required=False)
    


class RootPaymentMode(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    anonymous_enable = fields.Boolean(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    add_card_enabled = fields.Boolean(required=False)
    
    list = fields.List(fields.Nested(PaymentModeList, required=False), required=False)
    


class PaymentOptions(BaseSchema):
    # Payment swagger.json

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    


class PaymentOptionsResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    payment_options = fields.Nested(PaymentOptions, required=False)
    


class PayoutsResponse(BaseSchema):
    # Payment swagger.json

    
    unique_transfer_no = fields.Dict(required=False)
    
    transfer_type = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    more_attributes = fields.Dict(required=False)
    
    customers = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    payouts_aggregators = fields.List(fields.Dict(required=False), required=False)
    


class PayoutBankDetails(BaseSchema):
    # Payment swagger.json

    
    account_holder = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    account_type = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    


class PayoutRequest(BaseSchema):
    # Payment swagger.json

    
    transfer_type = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    bank_details = fields.Nested(PayoutBankDetails, required=False)
    
    users = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PayoutResponse(BaseSchema):
    # Payment swagger.json

    
    unique_transfer_no = fields.Str(required=False)
    
    transfer_type = fields.Str(required=False)
    
    payouts = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    bank_details = fields.Dict(required=False)
    
    payment_status = fields.Str(required=False)
    
    users = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    created = fields.Boolean(required=False)
    


class UpdatePayoutResponse(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    


class UpdatePayoutRequest(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    unique_external_id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


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
    
    aggregator = fields.Str(required=False)
    
    config = fields.Dict(required=False)
    


class SaveSubscriptionSetupIntentRequest(BaseSchema):
    # Payment swagger.json

    
    unique_external_id = fields.Str(required=False)
    


class SaveSubscriptionSetupIntentResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    


class BeneficiaryModeDetails(BaseSchema):
    # Payment swagger.json

    
    account_holder = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    wallet = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    


class AddBeneficiaryDetailsRequest(BaseSchema):
    # Payment swagger.json

    
    shipment_id = fields.Str(required=False)
    
    details = fields.Nested(BeneficiaryModeDetails, required=False)
    
    transfer_mode = fields.Str(required=False)
    
    delights = fields.Boolean(required=False)
    
    otp = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    


class RefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    


class NotFoundResourceError(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class IfscCodeResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    bank_name = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    


class OrderBeneficiaryDetails(BaseSchema):
    # Payment swagger.json

    
    account_holder = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    
    transfer_mode = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    delights_user_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    branch_name = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    


class OrderBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    show_beneficiary_details = fields.Boolean(required=False)
    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    


class PaymentConfirmationMode(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class PaymentConfirmationRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentConfirmationMode, required=False), required=False)
    


class PaymentConfirmationResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    


class CODdata(BaseSchema):
    # Payment swagger.json

    
    usages = fields.Int(required=False)
    
    limit = fields.Int(required=False)
    
    remaining_limit = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    


class GetUserCODLimitResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    user_cod_data = fields.Nested(CODdata, required=False)
    


class SetCODForUserRequest(BaseSchema):
    # Payment swagger.json

    
    mobileno = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    merchant_user_id = fields.Str(required=False)
    


class SetCODOptionResponse(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class RepaymentRequestDetails(BaseSchema):
    # Payment swagger.json

    
    outstanding_details_id = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    aggregator_transaction_id = fields.Str(required=False)
    
    fwd_shipment_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    current_status = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    payment_mode_identifier = fields.Str(required=False)
    


class RepaymentDetailsSerialiserPayAll(BaseSchema):
    # Payment swagger.json

    
    aggregator_order_id = fields.Str(required=False)
    
    total_amount = fields.Float(required=False)
    
    shipment_details = fields.List(fields.Nested(RepaymentRequestDetails, required=False), required=False)
    
    aggregator_transaction_id = fields.Str(required=False)
    
    extension_order_id = fields.Str(required=False)
    


class RepaymentResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    


class MerchantOnBoardingRequest(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    credit_line_id = fields.Str(required=False)
    


class MerchantOnBoardingResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    


