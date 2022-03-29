"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class ServiceabilityValidator:
    
    class getApplicationServiceability(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getEntityRegionView(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getListView(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getCompanyStoreView(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updateZoneControllerView(BaseSchema):
        
        zone_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class getZoneDataView(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
         
    
    class upsertZoneControllerView(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class upsertZoneControllerView(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    