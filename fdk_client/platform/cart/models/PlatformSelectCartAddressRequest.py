"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class PlatformSelectCartAddressRequest(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
