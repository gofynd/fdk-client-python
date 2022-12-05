"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .PaymentModeLogo import PaymentModeLogo





class IntentApp(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    package_name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    code = fields.Str(required=False)
    
