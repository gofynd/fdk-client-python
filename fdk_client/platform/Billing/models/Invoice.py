"""Billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InvoiceDetails import InvoiceDetails



from .InvoiceItems import InvoiceItems



class Invoice(BaseSchema):
    #  swagger.json

    
    invoice = fields.Nested(InvoiceDetails, required=False)
    
    invoice_items = fields.List(fields.Nested(InvoiceItems, required=False), required=False)
    
