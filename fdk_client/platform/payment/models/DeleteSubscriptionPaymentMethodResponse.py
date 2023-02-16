"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DeleteSubscriptionPaymentMethodResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
