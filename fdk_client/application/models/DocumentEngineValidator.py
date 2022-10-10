"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class DocumentEngineValidator:
    
    class getInvoiceByShipmentId(BaseSchema):
        
        shipment_id = fields.Str(required=False)
        
        parameters = fields.Nested(invoiceParameter, required=False)
         
    
    class getCreditNoteByShipmentId(BaseSchema):
        
        shipment_id = fields.Str(required=False)
        
        parameters = fields.Nested(creditNoteParameter, required=False)
         
    