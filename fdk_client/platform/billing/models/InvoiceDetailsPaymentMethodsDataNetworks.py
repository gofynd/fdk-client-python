"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InvoiceDetailsPaymentMethodsDataNetworks(BaseSchema):
    #  swagger.json

    
    available = fields.List(fields.Str(required=False), required=False)
    
    preferred = fields.Str(required=False)
    
