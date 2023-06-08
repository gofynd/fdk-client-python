

"""Partner Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        



class PartnerValidator:
    
    
    class subscribeExtension(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        entity = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        entity_id = fields.Str(required=False)
         
        
    
    class getExtensionsForCompany(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_size = fields.Float(required=False)
        
        tag = fields.Str(required=False)
        
        current_page = fields.Str(required=False)
        
        page_no = fields.Float(required=False)
        
        filter_by = fields.Str(required=False)
        
        query = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        is_application_level = fields.Str(required=False)
        
        is_saleschannel = fields.Str(required=False)
        
        extention_type = fields.Str(required=False)
         
        
    
    class getPublicExtension(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class getExtensionById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
         
        
    
    class deleteExtensionById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        message = fields.Str(required=False)
        
        uninstall_reason_type = fields.Str(required=False)
         
        
    
    class getPrivateExtensions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_size = fields.Float(required=False)
        
        page_no = fields.Float(required=False)
        
        query = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        installed = fields.Str(required=False)
         
        
    
    class getExtensionsSuggestions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_size = fields.Float(required=False)
         
        
    
    class getPartnerInvites(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        request_status = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
         
        
    
    class getPartnerRequestDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        invite_id = fields.Str(required=False)
         
        
    
    class modifyPartnerRequest(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        invite_id = fields.Str(required=False)
         
        
    
    class setupProducts(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        request_id = fields.Str(required=False)
         
        
    
    

