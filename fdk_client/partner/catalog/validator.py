

"""Catalog Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
    
    
        
        
        

class CatalogValidator:
    
    
    class partnerCompanyDetails(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class getCompanies(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
         
        
    
    

