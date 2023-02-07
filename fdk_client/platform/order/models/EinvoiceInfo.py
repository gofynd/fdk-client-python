"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EInvoice import EInvoice



from .EInvoice import EInvoice



class EinvoiceInfo(BaseSchema):
    #  swagger.json

    
    invoice = fields.Nested(EInvoice, required=False)
    
    credit_note = fields.Nested(EInvoice, required=False)
    
