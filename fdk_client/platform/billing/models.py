"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class SubscriptionChargeRes(BaseSchema):
    pass


class ChargeDetails(BaseSchema):
    pass


class ResourceNotFound(BaseSchema):
    pass


class CreateOneTimeCharge(BaseSchema):
    pass


class CreateOneTimeChargeResponse(BaseSchema):
    pass


class BadRequest(BaseSchema):
    pass


class CreateSubscriptionCharge(BaseSchema):
    pass


class CreateSubscriptionResponse(BaseSchema):
    pass


class EntityChargePrice(BaseSchema):
    pass


class ChargeRecurring(BaseSchema):
    pass


class SubscriptionTrialPeriod(BaseSchema):
    pass


class Charge(BaseSchema):
    pass


class OneTimeChargeItem(BaseSchema):
    pass


class ChargeLineItem(BaseSchema):
    pass


class EntitySubscription(BaseSchema):
    pass


class OneTimeChargeEntity(BaseSchema):
    pass


class EntityChargeRecurring(BaseSchema):
    pass


class EntityChargeDetails(BaseSchema):
    pass





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
    


class ResourceNotFound(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Raw(required=False)
    
    success = fields.Raw(required=False)
    


class CreateOneTimeCharge(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    charge = fields.Nested(OneTimeChargeItem, required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    


class CreateOneTimeChargeResponse(BaseSchema):
    # Billing swagger.json

    
    charge = fields.Nested(Charge, required=False)
    
    confirm_url = fields.Str(required=False)
    


class BadRequest(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


class CreateSubscriptionCharge(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    trial_days = fields.Int(required=False)
    
    line_items = fields.List(fields.Nested(ChargeLineItem, required=False), required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    


class CreateSubscriptionResponse(BaseSchema):
    # Billing swagger.json

    
    subscription = fields.Nested(EntitySubscription, required=False)
    
    confirm_url = fields.Str(required=False)
    


class EntityChargePrice(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    


class ChargeRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_time = fields.Float(required=False)
    


class SubscriptionTrialPeriod(BaseSchema):
    # Billing swagger.json

    
    start_date = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    


class Charge(BaseSchema):
    # Billing swagger.json

    
    final_charge = fields.Nested(OneTimeChargeEntity, required=False)
    


class OneTimeChargeItem(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    term = fields.Str(required=False)
    
    pricing_type = fields.Str(required=False)
    
    price = fields.Nested(EntityChargePrice, required=False)
    
    capped_amount = fields.Float(required=False)
    
    is_test = fields.Boolean(required=False)
    
    metadata = fields.Dict(required=False)
    


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
    


class EntityChargeRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    


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
    


