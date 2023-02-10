"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PaymentModeInfo(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
