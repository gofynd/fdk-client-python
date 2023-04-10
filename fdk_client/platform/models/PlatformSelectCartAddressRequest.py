"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PlatformSelectCartAddressRequest(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    

