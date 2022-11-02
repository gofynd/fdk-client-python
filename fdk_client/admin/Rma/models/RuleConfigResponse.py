"""Rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class RuleConfigResponse(BaseSchema):
    #  swagger.json

    
    response = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    
