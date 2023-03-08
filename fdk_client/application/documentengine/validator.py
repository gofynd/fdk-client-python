

"""DocumentEngine Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
                
from .models import invoiceParameter

    
    
        
                
from .models import creditNoteParameter


class DocumentEngineValidator:
    
    
    class getInvoiceByShipmentId(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
        
        parameters = fields.Nested(invoiceParameter, required=False)
         
        
    
    class getCreditNoteByShipmentId(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
        
        parameters = fields.Nested(creditNoteParameter, required=False)
         
        
    
    


