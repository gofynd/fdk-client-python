"""Billing Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class InternalServerError(BaseSchema):
    pass


class PlanRecurring(BaseSchema):
    pass


class Plan(BaseSchema):
    pass


class DetailList(BaseSchema):
    pass


class PlanTaxation(BaseSchema):
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


class ComponentsSchema(BaseSchema):
    pass


class PlanDetails(BaseSchema):
    pass





class InternalServerError(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


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
    


class DetailList(BaseSchema):
    # Billing swagger.json

    
    plans = fields.List(fields.Nested(Plan, required=False), required=False)
    
    trial_plan = fields.Nested(Plan, required=False)
    
    component_groups = fields.List(fields.Str(required=False), required=False)
    


class PlanTaxation(BaseSchema):
    # Billing swagger.json

    
    gst = fields.Float(required=False)
    


class OneTimeFees(BaseSchema):
    # Billing swagger.json

    
    developement = fields.Int(required=False, allow_none=True)
    
    marketing = fields.Int(required=False, allow_none=True)
    


class CreditLine(BaseSchema):
    # Billing swagger.json

    
    is_active = fields.Boolean(required=False)
    


class PlanMeta(BaseSchema):
    # Billing swagger.json

    
    plan_platform_display_name = fields.Str(required=False)
    


class FeatureConfig(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    


class PlanConfig(BaseSchema):
    # Billing swagger.json

    
    is_active = fields.Boolean(required=False)
    
    display_text = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    processing_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    feature_config = fields.Nested(FeatureConfig, required=False)
    
    _id = fields.Str(required=False)
    
    component_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    


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
    
    display_text = fields.Str(required=False)
    


class PlanDetails(BaseSchema):
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
    
    taxation = fields.Nested(PlanTaxation, required=False)
    
    one_time_fees = fields.Nested(OneTimeFees, required=False)
    
    credit_line = fields.Nested(CreditLine, required=False)
    
    current_status = fields.Str(required=False)
    
    meta = fields.Nested(PlanMeta, required=False)
    
    components = fields.List(fields.Nested(ComponentsSchema, required=False), required=False)
    


