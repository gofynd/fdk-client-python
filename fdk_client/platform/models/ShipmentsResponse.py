"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class ShipmentsResponse(BaseSchema):
    # OrderManage swagger.json

    
    stack_trace = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    exception = fields.Str(required=False)
    
    final_state = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    
