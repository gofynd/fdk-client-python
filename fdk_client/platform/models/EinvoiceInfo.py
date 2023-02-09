"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EInvoice import EInvoice

from .EInvoice import EInvoice


class EinvoiceInfo(BaseSchema):
    # Orders swagger.json

    
    credit_note = fields.Nested(EInvoice, required=False)
    
    invoice = fields.Nested(EInvoice, required=False)
    

