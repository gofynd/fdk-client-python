"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class CreateOrderErrorReponse(BaseSchema):
    # OrderManage swagger.json

    
    exception = fields.Str(required=False)
    
    info = fields.Raw(required=False)
    
    status = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    

