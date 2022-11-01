"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InvoiceCredSerializer import InvoiceCredSerializer



from .InvoiceCredSerializer import InvoiceCredSerializer



class InvoiceDetailsSerializer(BaseSchema):
    #  swagger.json

    
    e_invoice = fields.Nested(InvoiceCredSerializer, required=False)
    
    e_waybill = fields.Nested(InvoiceCredSerializer, required=False)
    
