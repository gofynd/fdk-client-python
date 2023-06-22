

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
        
        q = fields.Str(required=False)
         
        
    
    class getCompanyStoreView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class updateZoneControllerView(BaseSchema):
        
        
        zone_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getZoneDataView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
         
        
    
    class createZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getZoneListView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_number = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        name = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
        
        channel_ids = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        zone_id = fields.List(fields.Str(required=False), required=False)
         
        
    
    class getStore(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        store_uid = fields.Int(required=False)
         
        
    
    class getAllStores(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getOptimalLocations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class postRegionJobBulk(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getRegionJobBulk(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        current_page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getRegionJobBulkBatchId(BaseSchema):
        
        
        batch_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class upsertDpAccount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getDpAccount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        stage = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        transport_type = fields.Str(required=False)
         
        
    
    class updateDpRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class getDpRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class upsertDpRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getDpRuleInsert(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class upsertDpCompanyRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getDpCompanyRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

