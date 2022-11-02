"""Rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class RuleConfigRequest(BaseSchema):
    #  swagger.json

    
    channel = fields.Str(required=False)
    
    l2 = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    
    department = fields.Int(required=False)
    
    l1 = fields.Str(required=False)
    
    l3 = fields.Str(required=False)
    
