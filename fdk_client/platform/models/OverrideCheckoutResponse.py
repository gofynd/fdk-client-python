"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class OverrideCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.Dict(required=False)
    
    success = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    cart = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    

