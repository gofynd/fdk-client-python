"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SubscriptionInvoiceSettings(BaseSchema):
    #  swagger.json

    
    generation = fields.Boolean(required=False)
    
    charging = fields.Boolean(required=False)
    
