"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class E(BaseSchema):
    # Rewards swagger.json

    
    code = fields.Dict(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
