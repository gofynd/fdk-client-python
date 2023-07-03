

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
         
        
    
    class creditlineDataplatform(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class isCreditlinePlatform(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class invoiceType(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class invoiceListing(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class invoicePDF(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class asCnRefund(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class createSellerCreditNoteConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class deleteConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class channelDisplayName(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        filter_key = fields.Str(required=False)
         
        
    
    class getPdfUrlView(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class creditNoteDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getCustomerCreditBalance(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getCnConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class generateReportCustomerCn(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class downloadReportCustomerCn(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getReportingFilters(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        filter_key = fields.Str(required=False)
        
        affiliate_id = fields.Str(required=False)
         
        
    
    

