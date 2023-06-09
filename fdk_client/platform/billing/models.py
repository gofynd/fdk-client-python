"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class Page(BaseSchema):
    pass


class UnauthenticatedUser(BaseSchema):
    pass


class UnauthenticatedApplication(BaseSchema):
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


class Plan(BaseSchema):
    pass


class DetailedPlanComponents(BaseSchema):
    pass


class DetailedPlan(BaseSchema):
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


class InvoiceDetailsPaymentMethodsDataChecks(BaseSchema):
    pass


class InvoiceDetailsPaymentMethodsDataNetworks(BaseSchema):
    pass


class InvoiceDetailsPaymentMethodsDataThreeDSecureUsage(BaseSchema):
    pass


class InvoiceDetailsPaymentMethodsData(BaseSchema):
    pass


class InvoiceDetailsPaymentMethods(BaseSchema):
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





class Page(BaseSchema):
    # Billing swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class UnauthenticatedUser(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


class UnauthenticatedApplication(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


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
    


class DetailedPlanComponents(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    group = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    links = fields.Dict(required=False)
    
    enabled = fields.Boolean(required=False)
    
    display_text = fields.Str(required=False)
    
    config = fields.Dict(required=False)
    


class DetailedPlan(BaseSchema):
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
    
    components = fields.List(fields.Nested(DetailedPlanComponents, required=False), required=False)
    


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
    


class InvoiceDetailsPaymentMethodsDataChecks(BaseSchema):
    # Billing swagger.json

    
    cvc_check = fields.Str(required=False)
    
    address_line1_check = fields.Str(required=False)
    
    address_postal_code_check = fields.Str(required=False)
    


class InvoiceDetailsPaymentMethodsDataNetworks(BaseSchema):
    # Billing swagger.json

    
    available = fields.List(fields.Str(required=False), required=False)
    
    preferred = fields.Str(required=False)
    


class InvoiceDetailsPaymentMethodsDataThreeDSecureUsage(BaseSchema):
    # Billing swagger.json

    
    supported = fields.Boolean(required=False)
    


class InvoiceDetailsPaymentMethodsData(BaseSchema):
    # Billing swagger.json

    
    brand = fields.Str(required=False)
    
    last4 = fields.Str(required=False)
    
    checks = fields.Nested(InvoiceDetailsPaymentMethodsDataChecks, required=False)
    
    wallet = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    funding = fields.Str(required=False)
    
    exp_year = fields.Int(required=False)
    
    networks = fields.Nested(InvoiceDetailsPaymentMethodsDataNetworks, required=False)
    
    exp_month = fields.Int(required=False)
    
    fingerprint = fields.Str(required=False)
    
    generated_from = fields.Str(required=False)
    
    three_d_secure_usage = fields.Nested(InvoiceDetailsPaymentMethodsDataThreeDSecureUsage, required=False)
    


class InvoiceDetailsPaymentMethods(BaseSchema):
    # Billing swagger.json

    
    id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    pg_payment_method_id = fields.Str(required=False)
    
    data = fields.Nested(InvoiceDetailsPaymentMethodsData, required=False)
    
    is_default = fields.Boolean(required=False)
    


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
    
    plan_data = fields.Dict(required=False)
    
    current_status = fields.Str(required=False)
    
    collection_method = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    latest_invoice = fields.Str(required=False)
    


class SubscriptionStatus(BaseSchema):
    # Billing swagger.json

    
    mandate_amount = fields.Float(required=False)
    
    is_enabled = fields.Boolean(required=False)
    
    subscription = fields.Nested(Subscription, required=False)
    


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
    


