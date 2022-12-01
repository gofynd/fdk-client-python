"""rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .Reason import Reason









class Rule(BaseSchema):
    #  swagger.json

    
    entity_type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    channel = fields.Int(required=False)
    
    reasons = fields.List(fields.Nested(Reason, required=False), required=False)
    
    qc_enabled = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    constraints = fields.Dict(required=False)
    
