"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SubscriptionPaymentMethodResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
