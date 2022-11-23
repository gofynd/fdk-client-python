"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class PaymentGatewayConfig(BaseSchema):
    #  swagger.json

    
    config_type = fields.Str(required=False)
    
    merchant_salt = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    secret = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
