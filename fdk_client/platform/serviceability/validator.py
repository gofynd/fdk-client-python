

"""Serviceability Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
    
    
        
    
    
        



class ServiceabilityValidator:
    
    
    class getEntityRegionView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getListView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        name = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
        
        channel_ids = fields.Str(required=False)
         
        
    
    class getCompanyStoreView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getZoneDataView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
         
        
    
    class updateZoneControllerView(BaseSchema):
        
        
        zone_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class insertZoneControllerView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getStore(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        store_uid = fields.Int(required=False)
         
        
    
    class getAllStores(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getOptimalLocations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

