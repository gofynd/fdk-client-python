

"""Common Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
    
    
        
        



class CommonValidator:
    
    
    class searchApplication(BaseSchema):
        
        
        authorization = fields.Str(required=False)
        
        query = fields.Str(required=False)
         
        
    
    class getLocations(BaseSchema):
        
        
        location_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    

