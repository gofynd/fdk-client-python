

"""FileStorage Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        

class FileStorageValidator:
    
    
    class appStartUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class appCompleteUpload(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class appCopyFiles(BaseSchema):
        
        
        sync = fields.Boolean(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class appbrowse(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
        
        search = fields.Str(required=False)
         
        
    
    class browsefiles(BaseSchema):
        
        
        namespace = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page = fields.Int(required=False)
        
        limit = fields.Int(required=False)
        
        search = fields.Str(required=False)
         
        
    
    class getPdfTypes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        country_code = fields.Str(required=False)
        
        store_os = fields.Boolean(required=False)
         
        
    
    class getDefaultPdfData(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        pdf_type_id = fields.Int(required=False)
        
        country_code = fields.Str(required=False)
         
        
    
    class updateHtmlTemplate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getDefaultHtmlTemplate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        pdf_type_id = fields.Int(required=False)
        
        format = fields.Str(required=False)
        
        country_code = fields.Str(required=False)
         
        
    
    class saveHtmlTemplate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getDefaultPdfTemplate(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        pdf_type_id = fields.Int(required=False)
        
        format = fields.Str(required=False)
        
        country_code = fields.Str(required=False)
         
        
    
    class generatePaymentReceipt(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    

