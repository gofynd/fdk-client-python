"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class RuleDefinition(BaseSchema):
    #  swagger.json

    
    is_exact = fields.Boolean(required=False)
    
    auto_apply = fields.Boolean(required=False)
    
    applicable_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    value_type = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    