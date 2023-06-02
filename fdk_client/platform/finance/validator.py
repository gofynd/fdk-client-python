

"""Finance Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        
    
    
        



class FinanceValidator:
    
    
    class generateReport(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class downloadReport(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getData(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getReason(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getReportList(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getAffiliate(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class downloadCreditDebitNote(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class paymentProcess(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    

