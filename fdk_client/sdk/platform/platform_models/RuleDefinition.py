"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema


















class RuleDefinition(BaseSchema):
    # Cart swagger.json

    
    value_type = fields.Str(required=False)
    
    auto_apply = fields.Boolean(required=False)
    
    currency_code = fields.Str(required=False)
    
    is_exact = fields.Boolean(required=False)
    
    applicable_on = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    

