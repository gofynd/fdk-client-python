"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class InvoiceDetailsPaymentMethodsDataChecks(BaseSchema):
    #  swagger.json

    
    cvc_check = fields.Str(required=False)
    
    address_line1_check = fields.Str(required=False)
    
    address_postal_code_check = fields.Str(required=False)
    
