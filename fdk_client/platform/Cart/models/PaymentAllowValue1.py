"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class PaymentAllowValue1(BaseSchema):
    #  swagger.json

    
    max = fields.Int(required=False)
    
