"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




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


class Plan(BaseSchema):
    pass


class SubscriptionTrialPeriod(BaseSchema):
    pass


class EntityChargePrice(BaseSchema):
    pass


class EntityChargeRecurring(BaseSchema):
    pass


class ChargeLineItem(BaseSchema):
    pass


class CreateSubscriptionCharge(BaseSchema):
    pass


class OneTimeChargeItem(BaseSchema):
    pass


class CreateOneTimeCharge(BaseSchema):
    pass


class CurrentPeriod(BaseSchema):
    pass


class SubscriptionCharge(BaseSchema):
    pass


class EntitySubscription(BaseSchema):
    pass


class OneTimeChargeEntity(BaseSchema):
    pass


class CreateOneTimeChargeResponse(BaseSchema):
    pass


class CreateSubscriptionResponse(BaseSchema):
    pass


class InvoiceDetailsPeriod(BaseSchema):
    pass


class InvoiceDetailsClient(BaseSchema):
    pass


class InvoiceDetailsStatusTrail(BaseSchema):
    pass


class InvoicePaymentMethod(BaseSchema):
    pass


class InvoiceDetails(BaseSchema):
    pass


class InvoiceItemsPlanRecurring(BaseSchema):
    pass


class InvoiceItemsPlan(BaseSchema):
    pass


class InvoiceItemsPeriod(BaseSchema):
    pass


class InvoiceItems(BaseSchema):
    pass


class Invoice(BaseSchema):
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


class SunscribePlan(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class SubscribePlanRes(BaseSchema):
    pass


class Features(BaseSchema):
    pass


class FeeComponents(BaseSchema):
    pass


class Details(BaseSchema):
    pass


class EntityResponse(BaseSchema):
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


class PaymentTransactionDetails(BaseSchema):
    pass


class PaymentItems(BaseSchema):
    pass


class GetPaymentOptions(BaseSchema):
    pass





class BadRequest(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


class ResourceNotFound(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


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
    


class Plan(BaseSchema):
    # Billing swagger.json

    
    recurring = fields.Nested(PlanRecurring, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
    plan_group = fields.Str(required=False)
    
    tag_lines = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    trial_period = fields.Float(required=False)
    
    addons = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    product_suite_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class SubscriptionTrialPeriod(BaseSchema):
    # Billing swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class EntityChargePrice(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    


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
    


class CurrentPeriod(BaseSchema):
    # Billing swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class SubscriptionCharge(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    recurring = fields.Nested(EntityChargeRecurring, required=False)
    
    capped_amount = fields.Float(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    billing_date = fields.Str(required=False)
    
    current_period = fields.Nested(CurrentPeriod, required=False)
    
    status = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
    metadata = fields.Dict(required=False)
    


class EntitySubscription(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    trial_days = fields.Int(required=False)
    
    trial_period = fields.Nested(SubscriptionTrialPeriod, required=False)
    
    metadata = fields.Dict(required=False)
    
    line_items = fields.List(fields.Nested(SubscriptionCharge, required=False), required=False)
    


class OneTimeChargeEntity(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    activated_on = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
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

    
    charge = fields.Nested(OneTimeChargeEntity, required=False)
    
    confirm_url = fields.Str(required=False)
    


class CreateSubscriptionResponse(BaseSchema):
    # Billing swagger.json

    
    subscription = fields.Nested(EntitySubscription, required=False)
    
    confirm_url = fields.Str(required=False)
    


class InvoiceDetailsPeriod(BaseSchema):
    # Billing swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class InvoiceDetailsClient(BaseSchema):
    # Billing swagger.json

    
    address_lines = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    


class InvoiceDetailsStatusTrail(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    


class InvoicePaymentMethod(BaseSchema):
    # Billing swagger.json

    
    pg_payment_method_id = fields.Str(required=False)
    


class InvoiceDetails(BaseSchema):
    # Billing swagger.json

    
    period = fields.Nested(InvoiceDetailsPeriod, required=False)
    
    client = fields.Nested(InvoiceDetailsClient, required=False)
    
    auto_advance = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    paid = fields.Boolean(required=False)
    
    attemp = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    collection_method = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    number = fields.Str(required=False)
    
    pg_data = fields.Dict(required=False)
    
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
    
    payment_method = fields.Nested(InvoicePaymentMethod, required=False)
    


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
    


class Invoice(BaseSchema):
    # Billing swagger.json

    
    invoice = fields.Nested(InvoiceDetails, required=False)
    
    invoice_items = fields.List(fields.Nested(InvoiceItems, required=False), required=False)
    


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
    
    plan_data = fields.Nested(Plan, required=False)
    
    current_status = fields.Str(required=False)
    
    collection_method = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    latest_invoice = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class SubscriptionStatus(BaseSchema):
    # Billing swagger.json

    
    is_enabled = fields.Boolean(required=False)
    
    subscription = fields.Nested(Subscription, required=False)
    
    latest_invoice = fields.Nested(InvoicesData, required=False)
    
    next_plan = fields.Nested(Plan, required=False)
    
    current_subscriptions = fields.List(fields.Nested(Subscription, required=False), required=False)
    
    mandate_amount = fields.Float(required=False)
    


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
    


class SubscriptionActivateReq(BaseSchema):
    # Billing swagger.json

    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_suite = fields.Str(required=False)
    
    plan_id = fields.Str(required=False)
    
    payment_method = fields.Str(required=False)
    


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
    


class SunscribePlan(BaseSchema):
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
    


class Features(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    group = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    display_text = fields.Str(required=False)
    


class FeeComponents(BaseSchema):
    # Billing swagger.json

    
    brand = fields.List(fields.Str(required=False), required=False)
    
    location = fields.List(fields.Str(required=False), required=False)
    
    channel = fields.List(fields.Dict(required=False), required=False)
    
    business_lead = fields.Str(required=False)
    
    settlement_type = fields.Str(required=False)
    
    settle_cycle_period = fields.Dict(required=False)
    
    components = fields.List(fields.Dict(required=False), required=False)
    


class Details(BaseSchema):
    # Billing swagger.json

    
    fee_components = fields.List(fields.Nested(FeeComponents, required=False), required=False)
    
    features = fields.List(fields.Nested(Features, required=False), required=False)
    


class EntityResponse(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    page = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    
    items = fields.List(fields.Nested(Details, required=False), required=False)
    


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
    
    credit_balance = fields.Int(required=False)
    
    data = fields.Nested(SubscriberData, required=False)
    


class Author(BaseSchema):
    # Billing swagger.json

    
    modified_by_details = fields.Dict(required=False)
    


class EndingBalance(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Int(required=False)
    
    old_entry_ref = fields.Str(required=False)
    


class PaymentData(BaseSchema):
    # Billing swagger.json

    
    transaction_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    aggregator_order_id = fields.Str(required=False)
    


class CreditTransaction(BaseSchema):
    # Billing swagger.json

    
    entity = fields.Dict(required=False)
    
    author = fields.Nested(Author, required=False)
    
    _id = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_test = fields.Boolean(required=False)
    
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
    


class SubscriptionMethods(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Str(required=False), required=False)
    


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

    
    total = fields.Int(required=False)
    
    credit_note_amount = fields.Int(required=False)
    
    taxable_amount = fields.Int(required=False)
    
    gst_amount = fields.Int(required=False)
    
    gross_total = fields.Int(required=False)
    
    gst = fields.Int(required=False)
    


class PlanChangeDetails(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(PlanChangeData, required=False)
    


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
    
    meta = fields.Nested(Meta, required=False)
    
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
    


