"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PaymentModeLogo(BaseSchema):
    #  swagger.json

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    
