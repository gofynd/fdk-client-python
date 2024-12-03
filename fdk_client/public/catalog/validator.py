

"""Catalog Public Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema



    
    
        
        
        
        
        
        

class CatalogValidator:
    
    
    class getTaxonomyByLevel(BaseSchema):
        
        
        level = fields.Int(required=False)
        
        l0_slug = fields.Str(required=False)
        
        l1_slug = fields.Str(required=False)
        
        l2_slug = fields.Str(required=False)
        
        l3_slug = fields.Str(required=False)
        
        limit = fields.Float(required=False)
         
        
    
    

