

"""Content Public Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema



    
    
    
    
        
    
    
        
    
    
    
        
    
    
    
    
    
        
    
    
    
        

class ContentValidator:
    
    
    class getBasicDetails(BaseSchema):
        
        pass 
        
    
    class getMenuContent(BaseSchema):
        
        pass 
        
    
    class getMenuContentByType(BaseSchema):
        
        
        type = fields.Str(required=False)
         
        
    
    class getCustomPage(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    class getFooterContent(BaseSchema):
        
        pass 
        
    
    class getHomePageContent(BaseSchema):
        
        
        page_type = fields.Str(required=False)
         
        
    
    class getNavbar(BaseSchema):
        
        pass 
        
    
    class getPricingBanner(BaseSchema):
        
        pass 
        
    
    class getAllTags(BaseSchema):
        
        pass 
        
    
    class getCredentialsByEntity(BaseSchema):
        
        
        entity_type = fields.Str(required=False)
         
        
    
    class getSDKDocumentation(BaseSchema):
        
        pass 
        
    
    class getSDKDocumentationByType(BaseSchema):
        
        
        type = fields.Str(required=False)
         
        
    
    

