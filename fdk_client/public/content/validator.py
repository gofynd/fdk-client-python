

"""Content Public Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema



    
    
        

class ContentValidator:
    
    
    class getCredentialsByEntity(BaseSchema):
        
        
        entity = fields.Str(required=False)
         
        
    
    

