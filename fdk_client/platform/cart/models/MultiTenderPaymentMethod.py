"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .MultiTenderPaymentMeta import MultiTenderPaymentMeta



class MultiTenderPaymentMethod(BaseSchema):
    #  swagger.json

    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
