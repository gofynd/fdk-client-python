

"""Partner Public Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema



    
    
        

class PartnerValidator:
    
    
    class getPanelExtensionDetails(BaseSchema):
        
        
        slug = fields.Str(required=False)
         
        
    
    

