"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .PaymentModeLogo import PaymentModeLogo





class IntentApp(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    package_name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    display_name = fields.Str(required=False)
    
