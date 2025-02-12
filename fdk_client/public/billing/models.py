"""Billing Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class TenureConfig(BaseSchema):
    pass


class TenureConfigData(BaseSchema):
    pass


class TenureConfigResponse(BaseSchema):
    pass


class ResourceNotFound(BaseSchema):
    pass


class PlanRecurring(BaseSchema):
    pass


class PlanTypes(BaseSchema):
    pass


class DetailList(BaseSchema):
    pass


class PlanTaxation(BaseSchema):
    pass


class CountryRes(BaseSchema):
    pass


class OneTimeFees(BaseSchema):
    pass


class CreditLine(BaseSchema):
    pass


class PlanMeta(BaseSchema):
    pass


class FeatureConfig(BaseSchema):
    pass


class PlanConfig(BaseSchema):
    pass


class FreeTier(BaseSchema):
    pass


class TransformQuantity(BaseSchema):
    pass


class ComponentsSchema(BaseSchema):
    pass


class PlanDetails(BaseSchema):
    pass


class Recurring(BaseSchema):
    pass


class Taxation(BaseSchema):
    pass


class PlanList(BaseSchema):
    pass


class TrialPlanDetails(BaseSchema):
    pass





class TenureConfig(BaseSchema):
    # Billing swagger.json

    
    display_name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    


class TenureConfigData(BaseSchema):
    # Billing swagger.json

    
    country = fields.Str(required=False)
    
    tenure_config = fields.List(fields.Nested(TenureConfig, required=False), required=False)
    


class TenureConfigResponse(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(TenureConfigData, required=False)
    


class ResourceNotFound(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    


class PlanRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Float(required=False)
    
    aggregate_usage = fields.Str(required=False)
    
    usage_type = fields.Str(required=False)
    


class PlanTypes(BaseSchema):
    # Billing swagger.json

    
    month = fields.List(fields.Nested(PlanDetails, required=False), required=False)
    
    quarter = fields.List(fields.Nested(PlanDetails, required=False), required=False)
    
    half_year = fields.List(fields.Nested(PlanDetails, required=False), required=False)
    
    year = fields.List(fields.Nested(PlanDetails, required=False), required=False)
    


class DetailList(BaseSchema):
    # Billing swagger.json

    
    plans = fields.Nested(PlanTypes, required=False)
    
    trial_plan = fields.Nested(TrialPlanDetails, required=False)
    


class PlanTaxation(BaseSchema):
    # Billing swagger.json

    
    gst = fields.Float(required=False)
    


class CountryRes(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class OneTimeFees(BaseSchema):
    # Billing swagger.json

    
    developement = fields.Int(required=False, allow_none=True)
    
    marketing = fields.Int(required=False, allow_none=True)
    


class CreditLine(BaseSchema):
    # Billing swagger.json

    
    is_active = fields.Boolean(required=False)
    


class PlanMeta(BaseSchema):
    # Billing swagger.json

    
    plan_platform_display_name = fields.Str(required=False, allow_none=True)
    


class FeatureConfig(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    
    hard_limit = fields.Int(required=False)
    
    soft_limit = fields.Int(required=False)
    


class PlanConfig(BaseSchema):
    # Billing swagger.json

    
    is_active = fields.Boolean(required=False)
    
    display_text = fields.Str(required=False, allow_none=True)
    
    is_default = fields.Boolean(required=False)
    
    processing_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    feature_config = fields.Nested(FeatureConfig, required=False)
    
    _id = fields.Str(required=False)
    
    component_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    billing_scheme = fields.Str(required=False)
    
    bill_type = fields.Str(required=False)
    
    price_ui_type = fields.Str(required=False)
    
    recurring = fields.Nested(PlanRecurring, required=False)
    
    transform_quantity = fields.Nested(TransformQuantity, required=False)
    
    free_tier = fields.Nested(FreeTier, required=False)
    
    currency = fields.Str(required=False)
    
    unit_amount = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    price_type = fields.Str(required=False)
    
    tiers = fields.List(fields.Dict(required=False), required=False)
    


class FreeTier(BaseSchema):
    # Billing swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Int(required=False)
    


class TransformQuantity(BaseSchema):
    # Billing swagger.json

    
    divide_by = fields.Int(required=False)
    
    round = fields.Str(required=False)
    


class ComponentsSchema(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    group = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    links = fields.Dict(required=False)
    
    config = fields.Nested(PlanConfig, required=False)
    
    is_active = fields.Boolean(required=False)
    
    display_text = fields.Str(required=False, allow_none=True)
    


class PlanDetails(BaseSchema):
    # Billing swagger.json

    
    activated_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    recurring = fields.Nested(PlanRecurring, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
    company_ids = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    platform = fields.Str(required=False, allow_none=True)
    
    plan_group = fields.Str(required=False)
    
    tag_lines = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
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
    
    taxation = fields.Nested(PlanTaxation, required=False)
    
    one_time_fees = fields.Nested(OneTimeFees, required=False)
    
    credit_line = fields.Nested(CreditLine, required=False)
    
    current_status = fields.Str(required=False)
    
    approved_by = fields.Str(required=False)
    
    meta = fields.Nested(PlanMeta, required=False)
    
    components = fields.List(fields.Nested(ComponentsSchema, required=False), required=False)
    


class Recurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Int(required=False)
    


class Taxation(BaseSchema):
    # Billing swagger.json

    
    gst = fields.Float(required=False)
    


class PlanList(BaseSchema):
    # Billing swagger.json

    
    approved_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    recurring = fields.Nested(Recurring, required=False)
    
    taxation = fields.Nested(Taxation, required=False)
    
    one_time_fees = fields.Nested(OneTimeFees, required=False)
    
    credit_line = fields.Nested(CreditLine, required=False)
    
    _id = fields.Str(required=False)
    
    product_suite_id = fields.Str(required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    plan_group = fields.Str(required=False)
    
    plan_group_id = fields.Str(required=False)
    
    tag_lines = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    trial_period = fields.Int(required=False)
    
    addons = fields.List(fields.Dict(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    country = fields.Nested(CountryRes, required=False)
    
    company_ids = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    platform = fields.Str(required=False, allow_none=True)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


class TrialPlanDetails(BaseSchema):
    # Billing swagger.json

    
    activated_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    recurring = fields.Nested(PlanRecurring, required=False)
    
    is_trial_plan = fields.Boolean(required=False)
    
    company_ids = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    platform = fields.Str(required=False, allow_none=True)
    
    plan_group = fields.Str(required=False)
    
    tag_lines = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
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
    
    taxation = fields.Nested(PlanTaxation, required=False)
    
    one_time_fees = fields.Nested(OneTimeFees, required=False)
    
    credit_line = fields.Nested(CreditLine, required=False)
    
    current_status = fields.Str(required=False)
    
    meta = fields.Nested(PlanMeta, required=False)
    
    components = fields.List(fields.Nested(ComponentsSchema, required=False), required=False)
    


