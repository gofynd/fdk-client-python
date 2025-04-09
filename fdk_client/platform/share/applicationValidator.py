

"""Share Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        

class ShareValidator:
    
    
    class createShortLink(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getShortLinks(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        created_by = fields.Str(required=False)
        
        active = fields.Str(required=False)
        
        short_url = fields.Str(required=False)
        
        original_url = fields.Str(required=False)
        
        title = fields.Str(required=False)
         
        
    
    class getShortLinkByHash(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        hash = fields.Str(required=False)
         
        
    
    class updateShortLinkById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getShortLinkClickStats(BaseSchema):
        
        
        surl_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    

