"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class CompanyInfo(BaseSchema):
    pass


class AddressDetails(BaseSchema):
    pass


class InvoiceData(BaseSchema):
    pass


class InvoiceDetailsData(BaseSchema):
    pass


class Client(BaseSchema):
    pass


class Period(BaseSchema):
    pass


class StatusTrail(BaseSchema):
    pass


class PaymentCollectRes(BaseSchema):
    pass


class SubscriptionChargeRes(BaseSchema):
    pass


class PostDowngradeRes(BaseSchema):
    pass


class DowngradeRes(BaseSchema):
    pass


class PaymentStatusData(BaseSchema):
    pass


class PaymentStatusResponse(BaseSchema):
    pass


class BadRequest(BaseSchema):
    pass


class ResourceNotFound(BaseSchema):
    pass


class InternalServerError(BaseSchema):
    pass


class CheckValidityResponse(BaseSchema):
    pass


class PlanRecurring(BaseSchema):
    pass


class PlanMeta(BaseSchema):
    pass


class CountryRes(BaseSchema):
    pass


class Plan(BaseSchema):
    pass


class SubscriptionTrialPeriod(BaseSchema):
    pass


class EntityChargePrice(BaseSchema):
    pass


class OneTimeChargeItem(BaseSchema):
    pass


class CreateOneTimeCharge(BaseSchema):
    pass


class ChargeRecurring(BaseSchema):
    pass


class ChargeDetails(BaseSchema):
    pass


class OneTimeChargeEntity(BaseSchema):
    pass


class CreateOneTimeChargeResponse(BaseSchema):
    pass


class Charge(BaseSchema):
    pass


class InvoiceDetailsStatusTrail(BaseSchema):
    pass


class InvoiceItemsPlanRecurring(BaseSchema):
    pass


class InvoiceItemsPlan(BaseSchema):
    pass


class InvoiceItemsPeriod(BaseSchema):
    pass


class InvoiceItems(BaseSchema):
    pass


class InvoicesDataClient(BaseSchema):
    pass


class InvoicesDataPeriod(BaseSchema):
    pass


class InvoicesDataPaymentMethod(BaseSchema):
    pass


class InvoicesData(BaseSchema):
    pass


class Invoices(BaseSchema):
    pass


class Phone(BaseSchema):
    pass


class SubscriptionBillingAddress(BaseSchema):
    pass


class SubscriptionCustomer(BaseSchema):
    pass


class SubscriptionCustomerCreate(BaseSchema):
    pass


class SubscriptionCurrentPeriod(BaseSchema):
    pass


class SubscriptionPauseCollection(BaseSchema):
    pass


class SubscriptionTrial(BaseSchema):
    pass


class SubscriptionInvoiceSettings(BaseSchema):
    pass


class Subscription(BaseSchema):
    pass


class SubscriptionStatus(BaseSchema):
    pass


class SubscriptionLimitApplication(BaseSchema):
    pass


class SubscriptionLimitMarketplace(BaseSchema):
    pass


class SubscriptionLimitOtherPlatform(BaseSchema):
    pass


class SubscriptionLimitTeam(BaseSchema):
    pass


class SubscriptionLimitProducts(BaseSchema):
    pass


class SubscriptionLimitExtensions(BaseSchema):
    pass


class SubscriptionLimitIntegrations(BaseSchema):
    pass


class SubscriptionLimit(BaseSchema):
    pass


class IntentReq(BaseSchema):
    pass


class PutIntentReq(BaseSchema):
    pass


class SubscriptionActivateReq(BaseSchema):
    pass


class SubscriptionActivateRes(BaseSchema):
    pass


class CancelSubscriptionReq(BaseSchema):
    pass


class CancelSubscriptionRes(BaseSchema):
    pass


class PlanStatusUpdateReq(BaseSchema):
    pass


class SubscribePlan(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class SubscribePlanRes(BaseSchema):
    pass


class EntityDetail(BaseSchema):
    pass


class PaymentOptions(BaseSchema):
    pass


class VerifyPaymentReq(BaseSchema):
    pass


class Documents(BaseSchema):
    pass


class BillingAddress(BaseSchema):
    pass


class Currency(BaseSchema):
    pass


class BusinessCountryInfo(BaseSchema):
    pass


class SubscriberData(BaseSchema):
    pass


class Subscriber(BaseSchema):
    pass


class AuthorModifiedDetails(BaseSchema):
    pass


class Author(BaseSchema):
    pass


class EndingBalance(BaseSchema):
    pass


class PaymentData(BaseSchema):
    pass


class CreditTransaction(BaseSchema):
    pass


class VerifyPaymentData(BaseSchema):
    pass


class VerifyPaymentRes(BaseSchema):
    pass


class DefaultMerchants(BaseSchema):
    pass


class GlobalSettingsPayment(BaseSchema):
    pass


class GlobalSettingsData(BaseSchema):
    pass


class GlobalSettings(BaseSchema):
    pass


class MethodChecks(BaseSchema):
    pass


class MethodNetworks(BaseSchema):
    pass


class MethodSecureUsage(BaseSchema):
    pass


class MethodDetails(BaseSchema):
    pass


class SubscriptionMethodData(BaseSchema):
    pass


class SubscriptionMethods(BaseSchema):
    pass


class ConfigPublicKey(BaseSchema):
    pass


class ConfigRes(BaseSchema):
    pass


class PlanChangeData(BaseSchema):
    pass


class PlanChangeDetails(BaseSchema):
    pass


class TransactionMeta(BaseSchema):
    pass


class PaymentTransactionDetails(BaseSchema):
    pass


class PaymentItems(BaseSchema):
    pass


class GetPaymentOptions(BaseSchema):
    pass


class TopupReq(BaseSchema):
    pass


class SetupMandateReq(BaseSchema):
    pass


class SetupPaymentReq(BaseSchema):
    pass


class SubscriptionRenewReq(BaseSchema):
    pass


class RenewMeta(BaseSchema):
    pass


class SubscriptionMethodsReq(BaseSchema):
    pass


class CreditTransactionResponse(BaseSchema):
    pass


class DowngradePlanReq(BaseSchema):
    pass


class Taxation(BaseSchema):
    pass


class OneTimeFees(BaseSchema):
    pass


class CreditLine(BaseSchema):
    pass


class StatusMessage(BaseSchema):
    pass


class PaymentCollectReq(BaseSchema):
    pass


class SubscriptionRenewResMeta(BaseSchema):
    pass


class SubscriptionRenewRes(BaseSchema):
    pass


class SetupIntentRes(BaseSchema):
    pass


class SetupIntentData(BaseSchema):
    pass


class SetupPayment(BaseSchema):
    pass


class PaymentMethodOptions(BaseSchema):
    pass


class Card(BaseSchema):
    pass


class MandateOptions(BaseSchema):
    pass


class Message(BaseSchema):
    pass


class TopupRes(BaseSchema):
    pass


class CancelTopupReq(BaseSchema):
    pass


class CancelTopupRes(BaseSchema):
    pass


class DefaultReq(BaseSchema):
    pass


class EntityChargeRecurring(BaseSchema):
    pass


class ChargeLineItem(BaseSchema):
    pass


class CreateSubscriptionCharge(BaseSchema):
    pass


class EntityChargeDetails(BaseSchema):
    pass


class EntitySubscription(BaseSchema):
    pass


class CreateSubscriptionResponse(BaseSchema):
    pass





class CompanyInfo(BaseSchema):
    # Billing swagger.json

    
    company_name = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    address_details = fields.Nested(AddressDetails, required=False)
    
    pan = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    cin = fields.Str(required=False)
    


class AddressDetails(BaseSchema):
    # Billing swagger.json

    
    address_line_1 = fields.Str(required=False)
    
    address_line_2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class InvoiceData(BaseSchema):
    # Billing swagger.json

    
    invoice = fields.Nested(InvoiceDetailsData, required=False)
    
    invoice_items = fields.List(fields.Nested(InvoiceItems, required=False), required=False)
    
    shopsense_details = fields.Nested(CompanyInfo, required=False)
    


class InvoiceDetailsData(BaseSchema):
    # Billing swagger.json

    
    attemp = fields.Float(required=False, allow_none=True)
    
    documents = fields.Dict(required=False)
    
    payment = fields.Dict(required=False)
    
    period = fields.Nested(Period, required=False)
    
    client = fields.Nested(Client, required=False)
    
    discount = fields.Dict(required=False)
    
    taxation = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    auto_advance = fields.Boolean(required=False)
    
    collection_method = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    number = fields.Str(required=False)
    
    paid = fields.Boolean(required=False)
    
    pg_data = fields.Dict(required=False)
    
    receipt_number = fields.Str(required=False)
    
    statement_descriptor = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    status_trail = fields.List(fields.Nested(StatusTrail, required=False), required=False)
    
    subtotal = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    old_settlement = fields.Float(required=False, allow_none=True)
    
    credit_balance = fields.Float(required=False, allow_none=True)
    
    subscription = fields.Str(required=False)
    
    attempt = fields.Float(required=False)
    
    next_action_time = fields.Str(required=False)
    
    credit_note_amount = fields.Float(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    invoice_type = fields.Str(required=False)
    


class Client(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    address_lines = fields.List(fields.Str(required=False), required=False)
    


class Period(BaseSchema):
    # Billing swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class StatusTrail(BaseSchema):
    # Billing swagger.json

    
    value = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class PaymentCollectRes(BaseSchema):
    # Billing swagger.json

    
    transaction_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    


class SubscriptionChargeRes(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    product_suit_id = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    trial_days = fields.Float(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    line_items = fields.List(fields.Dict(required=False), required=False)
    


class PostDowngradeRes(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(DowngradeRes, required=False)
    


class DowngradeRes(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    activated = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    request_user_id = fields.Str(required=False)
    
    subscription_id = fields.Str(required=False)
    


class PaymentStatusData(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    webhook_response = fields.List(fields.Raw(required=False), required=False)
    
    aggregator_status = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    


class PaymentStatusResponse(BaseSchema):
    # Billing swagger.json

    
    status = fields.Str(required=False)
    
    data = fields.Nested(PaymentStatusData, required=False)
    


class BadRequest(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


class ResourceNotFound(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Raw(required=False)
    
    success = fields.Raw(required=False)
    


class InternalServerError(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class CheckValidityResponse(BaseSchema):
    # Billing swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    discount_amount = fields.Float(required=False)
    


class PlanRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Float(required=False)
    


class PlanMeta(BaseSchema):
    # Billing swagger.json

    
    seller_status = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    plan_platform_display_name = fields.Str(required=False, allow_none=True)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class CountryRes(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class Plan(BaseSchema):
    # Billing swagger.json

    
    fee_components = fields.List(fields.Dict(required=False), required=False)
    
    recurring = fields.Nested(PlanRecurring, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
    plan_group = fields.Str(required=False)
    
    tag_lines = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    approved_by = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    trial_period = fields.Float(required=False)
    
    addons = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    country = fields.Nested(CountryRes, required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    product_suite_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    taxation = fields.Nested(Taxation, required=False)
    
    one_time_fees = fields.Nested(OneTimeFees, required=False)
    
    credit_line = fields.Nested(CreditLine, required=False)
    
    current_status = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    company_ids = fields.List(fields.Str(required=False, allow_none=True), required=False)
    
    platform = fields.Str(required=False, allow_none=True)
    
    activated_on = fields.Str(required=False)
    
    meta = fields.Nested(PlanMeta, required=False)
    
    created_by = fields.Str(required=False)
    


class SubscriptionTrialPeriod(BaseSchema):
    # Billing swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class EntityChargePrice(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    


class OneTimeChargeItem(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    capped_amount = fields.Float(required=False)
    
    is_test = fields.Boolean(required=False)
    
    metadata = fields.Dict(required=False)
    


class CreateOneTimeCharge(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    charge = fields.Nested(OneTimeChargeItem, required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    


class ChargeRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_time = fields.Float(required=False)
    


class ChargeDetails(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    charge_type = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    recurring = fields.Nested(ChargeRecurring, required=False)
    
    status = fields.Str(required=False)
    
    capped_amount = fields.Float(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    billing_date = fields.Str(required=False)
    
    current_period = fields.Nested(SubscriptionTrialPeriod, required=False)
    
    modified_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
    company_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    __v = fields.Float(required=False)
    


class OneTimeChargeEntity(BaseSchema):
    # Billing swagger.json

    
    term = fields.Str(required=False)
    
    charge_type = fields.Str(required=False)
    
    capped_amount = fields.Float(required=False)
    
    billing_date = fields.Str(required=False, allow_none=True)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    activated_on = fields.Str(required=False, allow_none=True)
    
    cancelled_on = fields.Str(required=False, allow_none=True)
    
    metadata = fields.Dict(required=False)
    
    return_url = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
    pricing_type = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    


class CreateOneTimeChargeResponse(BaseSchema):
    # Billing swagger.json

    
    charge = fields.Nested(Charge, required=False)
    
    confirm_url = fields.Str(required=False)
    


class Charge(BaseSchema):
    # Billing swagger.json

    
    final_charge = fields.Nested(OneTimeChargeEntity, required=False)
    


class InvoiceDetailsStatusTrail(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    


class InvoiceItemsPlanRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Int(required=False)
    


class InvoiceItemsPlan(BaseSchema):
    # Billing swagger.json

    
    recurring = fields.Nested(InvoiceItemsPlanRecurring, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
    plan_group = fields.Str(required=False)
    
    tag_lines = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    trial_period = fields.Int(required=False)
    
    addons = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    product_suite_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class InvoiceItemsPeriod(BaseSchema):
    # Billing swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class InvoiceItems(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    plan = fields.Nested(InvoiceItemsPlan, required=False)
    
    name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    period = fields.Nested(InvoiceItemsPeriod, required=False)
    
    unit_amount = fields.Float(required=False)
    
    amount = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    invoice_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class InvoicesDataClient(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    address_lines = fields.List(fields.Str(required=False), required=False)
    


class InvoicesDataPeriod(BaseSchema):
    # Billing swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class InvoicesDataPaymentMethod(BaseSchema):
    # Billing swagger.json

    
    pg_payment_method_id = fields.Str(required=False)
    


class InvoicesData(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    documents = fields.Dict(required=False)
    
    payment = fields.Dict(required=False)
    
    old_settlement = fields.Float(required=False, allow_none=True)
    
    credit_balance = fields.Float(required=False, allow_none=True)
    
    discount = fields.Dict(required=False)
    
    taxation = fields.Dict(required=False)
    
    credit_note_amount = fields.Float(required=False)
    
    client = fields.Nested(InvoicesDataClient, required=False)
    
    auto_advance = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    paid = fields.Boolean(required=False)
    
    attemp = fields.Int(required=False)
    
    collection_method = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    number = fields.Str(required=False)
    
    pg_data = fields.Dict(required=False)
    
    period = fields.Nested(InvoicesDataPeriod, required=False)
    
    receipt_number = fields.Str(required=False)
    
    statement_descriptor = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    status_trail = fields.List(fields.Nested(InvoiceDetailsStatusTrail, required=False), required=False)
    
    subtotal = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    subscription = fields.Str(required=False)
    
    next_action_time = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    hash_identifier = fields.Str(required=False)
    
    payment_method = fields.Nested(InvoicesDataPaymentMethod, required=False)
    
    invoice_items = fields.List(fields.Nested(InvoiceItems, required=False), required=False)
    
    invoice_type = fields.Str(required=False)
    


class Invoices(BaseSchema):
    # Billing swagger.json

    
    data = fields.List(fields.Nested(InvoicesData, required=False), required=False)
    
    start = fields.Int(required=False)
    
    end = fields.Int(required=False)
    
    limit = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class Phone(BaseSchema):
    # Billing swagger.json

    
    phone_number = fields.Str(required=False)
    
    phone_country_code = fields.Str(required=False)
    


class SubscriptionBillingAddress(BaseSchema):
    # Billing swagger.json

    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    line1 = fields.Str(required=False)
    
    line2 = fields.Str(required=False)
    
    postal_code = fields.Str(required=False)
    


class SubscriptionCustomer(BaseSchema):
    # Billing swagger.json

    
    phone = fields.Nested(Phone, required=False)
    
    billing_address = fields.Nested(SubscriptionBillingAddress, required=False)
    
    _id = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    documents = fields.Dict(required=False)
    
    consent = fields.Boolean(required=False)
    
    comms = fields.Boolean(required=False)
    
    credit_balance = fields.Int(required=False, allow_none=True)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    


class SubscriptionCustomerCreate(BaseSchema):
    # Billing swagger.json

    
    phone = fields.Nested(Phone, required=False)
    
    billing_address = fields.Nested(SubscriptionBillingAddress, required=False)
    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class SubscriptionCurrentPeriod(BaseSchema):
    # Billing swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class SubscriptionPauseCollection(BaseSchema):
    # Billing swagger.json

    
    behavior = fields.Str(required=False)
    
    resume_at = fields.Str(required=False)
    


class SubscriptionTrial(BaseSchema):
    # Billing swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class SubscriptionInvoiceSettings(BaseSchema):
    # Billing swagger.json

    
    generation = fields.Boolean(required=False)
    
    charging = fields.Boolean(required=False)
    


class Subscription(BaseSchema):
    # Billing swagger.json

    
    meta = fields.Dict(required=False)
    
    current_period = fields.Nested(SubscriptionCurrentPeriod, required=False)
    
    pause_collection = fields.Nested(SubscriptionPauseCollection, required=False)
    
    trial = fields.Nested(SubscriptionTrial, required=False)
    
    invoice_settings = fields.Nested(SubscriptionInvoiceSettings, required=False)
    
    is_active = fields.Boolean(required=False)
    
    cancel_at_period_end = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    product_suite_id = fields.Str(required=False)
    
    is_eligible_for_plan_change = fields.Boolean(required=False)
    
    plan_data = fields.Nested(Plan, required=False)
    
    current_status = fields.Str(required=False)
    
    collection_method = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    latest_invoice = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    freezed = fields.Boolean(required=False)
    
    cancel_at = fields.Str(required=False)
    
    canceled_at = fields.Str(required=False)
    


class SubscriptionStatus(BaseSchema):
    # Billing swagger.json

    
    is_enabled = fields.Boolean(required=False)
    
    subscription = fields.Nested(Subscription, required=False)
    
    latest_invoice = fields.Nested(InvoicesData, required=False)
    
    next_plan = fields.Nested(Plan, required=False)
    
    current_subscriptions = fields.List(fields.Nested(Subscription, required=False), required=False)
    
    mandate_amount = fields.Float(required=False)
    
    message = fields.Str(required=False)
    


class SubscriptionLimitApplication(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    
    hard_limit = fields.Int(required=False)
    
    soft_limit = fields.Int(required=False)
    


class SubscriptionLimitMarketplace(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    


class SubscriptionLimitOtherPlatform(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    


class SubscriptionLimitTeam(BaseSchema):
    # Billing swagger.json

    
    limit = fields.Int(required=False)
    


class SubscriptionLimitProducts(BaseSchema):
    # Billing swagger.json

    
    bulk = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    


class SubscriptionLimitExtensions(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    


class SubscriptionLimitIntegrations(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    


class SubscriptionLimit(BaseSchema):
    # Billing swagger.json

    
    application = fields.Nested(SubscriptionLimitApplication, required=False)
    
    marketplace = fields.Nested(SubscriptionLimitMarketplace, required=False)
    
    other_platform = fields.Nested(SubscriptionLimitOtherPlatform, required=False)
    
    team = fields.Nested(SubscriptionLimitTeam, required=False)
    
    products = fields.Nested(SubscriptionLimitProducts, required=False)
    
    extensions = fields.Nested(SubscriptionLimitExtensions, required=False)
    
    integrations = fields.Nested(SubscriptionLimitIntegrations, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    


class IntentReq(BaseSchema):
    # Billing swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    


class PutIntentReq(BaseSchema):
    # Billing swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    setup_intent_id = fields.Str(required=False)
    
    payment_method_id = fields.Str(required=False)
    
    set_default = fields.Boolean(required=False)
    


class SubscriptionActivateReq(BaseSchema):
    # Billing swagger.json

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    payment_method = fields.Str(required=False)
    
    subscription_id = fields.Str(required=False)
    
    coupon = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class SubscriptionActivateRes(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(Subscription, required=False)
    


class CancelSubscriptionReq(BaseSchema):
    # Billing swagger.json

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    subscription_id = fields.Str(required=False)
    


class CancelSubscriptionRes(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(Subscription, required=False)
    


class PlanStatusUpdateReq(BaseSchema):
    # Billing swagger.json

    
    plan_id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    seller_status = fields.Str(required=False)
    


class SubscribePlan(BaseSchema):
    # Billing swagger.json

    
    entity_type = fields.Str(required=False)
    
    collection_type = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    


class Meta(BaseSchema):
    # Billing swagger.json

    
    subscribe = fields.Boolean(required=False)
    
    is_custom_plan = fields.Boolean(required=False)
    
    is_plan_upgrade = fields.Boolean(required=False)
    


class SubscribePlanRes(BaseSchema):
    # Billing swagger.json

    
    redirect_url = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    


class EntityDetail(BaseSchema):
    # Billing swagger.json

    
    entity = fields.Str(required=False)
    
    item = fields.Nested(Subscription, required=False)
    


class PaymentOptions(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    aggregator_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class VerifyPaymentReq(BaseSchema):
    # Billing swagger.json

    
    razorpay_payment_id = fields.Str(required=False)
    
    razorpay_order_id = fields.Str(required=False)
    
    razorpay_signature = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    provider_type = fields.Str(required=False)
    


class Documents(BaseSchema):
    # Billing swagger.json

    
    pan = fields.Str(required=False)
    
    gst = fields.Str(required=False)
    


class BillingAddress(BaseSchema):
    # Billing swagger.json

    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    line1 = fields.Str(required=False)
    
    line2 = fields.Str(required=False)
    
    postal_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class Currency(BaseSchema):
    # Billing swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class BusinessCountryInfo(BaseSchema):
    # Billing swagger.json

    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    currency = fields.Nested(Currency, required=False)
    
    timezone = fields.Str(required=False)
    


class SubscriberData(BaseSchema):
    # Billing swagger.json

    
    pg_user_exists = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    pg_customer_id = fields.Str(required=False)
    
    default_payment_method = fields.Str(required=False)
    


class Subscriber(BaseSchema):
    # Billing swagger.json

    
    documents = fields.Nested(Documents, required=False)
    
    phone = fields.Dict(required=False)
    
    billing_address = fields.Nested(BillingAddress, required=False)
    
    consent = fields.Boolean(required=False)
    
    comms = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    credit_balance = fields.Int(required=False, allow_none=True)
    
    data = fields.Nested(SubscriberData, required=False)
    


class AuthorModifiedDetails(BaseSchema):
    # Billing swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    is_admin = fields.Boolean(required=False)
    


class Author(BaseSchema):
    # Billing swagger.json

    
    modified_by_details = fields.Nested(AuthorModifiedDetails, required=False)
    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    


class EndingBalance(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Int(required=False)
    
    old_entry_ref = fields.Str(required=False, allow_none=True)
    


class PaymentData(BaseSchema):
    # Billing swagger.json

    
    transaction_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    receipt_date = fields.Str(required=False)
    
    unique_transaction_reference = fields.Str(required=False)
    


class CreditTransaction(BaseSchema):
    # Billing swagger.json

    
    entity = fields.Dict(required=False)
    
    author = fields.Nested(Author, required=False)
    
    _id = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_test = fields.Str(required=False)
    
    ending_balance = fields.Nested(EndingBalance, required=False)
    
    payment = fields.Nested(PaymentData, required=False)
    
    type = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class VerifyPaymentData(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    subscriber = fields.Nested(Subscriber, required=False)
    
    credit_transaction = fields.Nested(CreditTransaction, required=False)
    


class VerifyPaymentRes(BaseSchema):
    # Billing swagger.json

    
    status = fields.Str(required=False)
    
    data = fields.Nested(VerifyPaymentData, required=False)
    


class DefaultMerchants(BaseSchema):
    # Billing swagger.json

    
    stripe = fields.Str(required=False)
    


class GlobalSettingsPayment(BaseSchema):
    # Billing swagger.json

    
    default_merchants = fields.Nested(DefaultMerchants, required=False)
    


class GlobalSettingsData(BaseSchema):
    # Billing swagger.json

    
    payment = fields.Nested(GlobalSettingsPayment, required=False)
    
    freeze_panel = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class GlobalSettings(BaseSchema):
    # Billing swagger.json

    
    status = fields.Str(required=False)
    
    data = fields.Nested(GlobalSettingsData, required=False)
    


class MethodChecks(BaseSchema):
    # Billing swagger.json

    
    address_line1_check = fields.Str(required=False)
    
    address_postal_code_check = fields.Str(required=False)
    
    cvc_check = fields.Str(required=False)
    


class MethodNetworks(BaseSchema):
    # Billing swagger.json

    
    available = fields.List(fields.Str(required=False), required=False)
    
    preferred = fields.Str(required=False, allow_none=True)
    


class MethodSecureUsage(BaseSchema):
    # Billing swagger.json

    
    supported = fields.Boolean(required=False)
    


class MethodDetails(BaseSchema):
    # Billing swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    mandate_available = fields.Boolean(required=False)
    
    mandate_amount = fields.Float(required=False)
    
    pg_payment_method_id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    data = fields.Nested(SubscriptionMethodData, required=False)
    


class SubscriptionMethodData(BaseSchema):
    # Billing swagger.json

    
    brand = fields.Str(required=False)
    
    checks = fields.Nested(MethodChecks, required=False)
    
    country = fields.Str(required=False)
    
    exp_month = fields.Float(required=False)
    
    exp_year = fields.Float(required=False)
    
    fingerprint = fields.Str(required=False)
    
    funding = fields.Str(required=False)
    
    generated_from = fields.Str(required=False, allow_none=True)
    
    last4 = fields.Str(required=False)
    
    networks = fields.Nested(MethodNetworks, required=False)
    
    three_d_secure_usage = fields.Nested(MethodSecureUsage, required=False)
    
    wallet = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class SubscriptionMethods(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(MethodDetails, required=False), required=False)
    


class ConfigPublicKey(BaseSchema):
    # Billing swagger.json

    
    public_key = fields.Str(required=False)
    


class ConfigRes(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    aggregator = fields.Str(required=False)
    
    config = fields.Nested(ConfigPublicKey, required=False)
    


class PlanChangeData(BaseSchema):
    # Billing swagger.json

    
    total = fields.Float(required=False)
    
    credit_note_amount = fields.Float(required=False)
    
    settlement = fields.Float(required=False)
    
    taxable_amount = fields.Float(required=False)
    
    gst_amount = fields.Float(required=False)
    
    gross_total = fields.Float(required=False)
    
    gst = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    


class PlanChangeDetails(BaseSchema):
    # Billing swagger.json

    
    status = fields.Str(required=False)
    
    data = fields.Nested(PlanChangeData, required=False)
    


class TransactionMeta(BaseSchema):
    # Billing swagger.json

    
    invoice_id = fields.Str(required=False)
    


class PaymentTransactionDetails(BaseSchema):
    # Billing swagger.json

    
    aggregator = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    entity_type = fields.Str(required=False)
    
    collection_type = fields.Str(required=False)
    
    meta = fields.Nested(TransactionMeta, required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class PaymentItems(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    


class GetPaymentOptions(BaseSchema):
    # Billing swagger.json

    
    payment_options = fields.List(fields.Nested(PaymentItems, required=False), required=False)
    


class TopupReq(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    provider_type = fields.Str(required=False)
    


class SetupMandateReq(BaseSchema):
    # Billing swagger.json

    
    intent_id = fields.Str(required=False)
    
    payment_method_id = fields.Str(required=False)
    


class SetupPaymentReq(BaseSchema):
    # Billing swagger.json

    
    payment_method = fields.Str(required=False)
    
    payment_id = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    invoice_id = fields.Str(required=False)
    


class SubscriptionRenewReq(BaseSchema):
    # Billing swagger.json

    
    invoice_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    collection_type = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    meta = fields.Nested(RenewMeta, required=False)
    


class RenewMeta(BaseSchema):
    # Billing swagger.json

    
    invoice_payment = fields.Boolean(required=False)
    
    renew = fields.Boolean(required=False)
    


class SubscriptionMethodsReq(BaseSchema):
    # Billing swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    setup_intent_id = fields.Str(required=False)
    
    pg_payment_method_id = fields.Str(required=False)
    
    set_default = fields.Boolean(required=False)
    


class CreditTransactionResponse(BaseSchema):
    # Billing swagger.json

    
    total = fields.Int(required=False)
    
    limit = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    pages = fields.Int(required=False)
    
    items = fields.List(fields.Nested(CreditTransaction, required=False), required=False)
    


class DowngradePlanReq(BaseSchema):
    # Billing swagger.json

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    platform = fields.Str(required=False, allow_none=True)
    


class Taxation(BaseSchema):
    # Billing swagger.json

    
    gst = fields.Float(required=False)
    


class OneTimeFees(BaseSchema):
    # Billing swagger.json

    
    developement = fields.Int(required=False, allow_none=True)
    
    marketing = fields.Int(required=False, allow_none=True)
    


class CreditLine(BaseSchema):
    # Billing swagger.json

    
    is_active = fields.Boolean(required=False)
    


class StatusMessage(BaseSchema):
    # Billing swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    


class PaymentCollectReq(BaseSchema):
    # Billing swagger.json

    
    transaction_id = fields.Str(required=False)
    
    credit_balance = fields.Boolean(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False)
    
    payment_method = fields.Str(required=False)
    
    invoice_id = fields.Str(required=False)
    


class SubscriptionRenewResMeta(BaseSchema):
    # Billing swagger.json

    
    invoice_payment = fields.Boolean(required=False)
    
    renew = fields.Boolean(required=False)
    


class SubscriptionRenewRes(BaseSchema):
    # Billing swagger.json

    
    redirect_url = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    meta = fields.Nested(SubscriptionRenewResMeta, required=False)
    


class SetupIntentRes(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(SetupIntentData, required=False)
    


class SetupIntentData(BaseSchema):
    # Billing swagger.json

    
    id = fields.Str(required=False)
    
    client_secret = fields.Str(required=False)
    
    customer = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class SetupPayment(BaseSchema):
    # Billing swagger.json

    
    id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    customer = fields.Str(required=False)
    
    client_secret = fields.Str(required=False)
    
    payment_method = fields.Str(required=False)
    
    mandate = fields.Str(required=False)
    
    payment_method_options = fields.Nested(PaymentMethodOptions, required=False)
    


class PaymentMethodOptions(BaseSchema):
    # Billing swagger.json

    
    card = fields.Nested(Card, required=False)
    


class Card(BaseSchema):
    # Billing swagger.json

    
    mandate_options = fields.Nested(MandateOptions, required=False)
    


class MandateOptions(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Int(required=False)
    


class Message(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


class TopupRes(BaseSchema):
    # Billing swagger.json

    
    status = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    transaction_id = fields.Str(required=False)
    


class CancelTopupReq(BaseSchema):
    # Billing swagger.json

    
    order_id = fields.Str(required=False)
    


class CancelTopupRes(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    
    aggregator_status = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    


class DefaultReq(BaseSchema):
    # Billing swagger.json

    
    payment_method_id = fields.Str(required=False)
    


class EntityChargeRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    


class ChargeLineItem(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    recurring = fields.Nested(EntityChargeRecurring, required=False)
    
    capped_amount = fields.Float(required=False)
    
    trial_days = fields.Int(required=False)
    
    is_test = fields.Boolean(required=False)
    
    metadata = fields.Dict(required=False)
    


class CreateSubscriptionCharge(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    trial_days = fields.Int(required=False)
    
    line_items = fields.List(fields.Nested(ChargeLineItem, required=False), required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    


class EntityChargeDetails(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    subscription_id = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    charge_type = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    recurring = fields.Nested(ChargeRecurring, required=False)
    
    status = fields.Str(required=False)
    
    capped_amount = fields.Float(required=False)
    
    activated_on = fields.Str(required=False, allow_none=True)
    
    cancelled_on = fields.Str(required=False, allow_none=True)
    
    billing_date = fields.Str(required=False, allow_none=True)
    
    current_period = fields.Nested(SubscriptionTrialPeriod, required=False)
    
    modified_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
    company_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    __v = fields.Float(required=False)
    


class EntitySubscription(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    product_suit_id = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    trial_days = fields.Float(required=False)
    
    is_test = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    line_items = fields.List(fields.Nested(EntityChargeDetails, required=False), required=False)
    
    return_url = fields.Str(required=False)
    


class CreateSubscriptionResponse(BaseSchema):
    # Billing swagger.json

    
    subscription = fields.Nested(EntitySubscription, required=False)
    
    confirm_url = fields.Str(required=False)
    


