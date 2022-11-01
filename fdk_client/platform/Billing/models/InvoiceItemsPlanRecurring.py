"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InvoiceItemsPlanRecurring(BaseSchema):
    #  swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Int(required=False)
    
