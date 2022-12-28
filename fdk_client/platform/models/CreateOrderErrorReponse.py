"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class CreateOrderErrorReponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    info = fields.Raw(required=False)
    
    stack_trace = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    meta = fields.Str(required=False)
    

