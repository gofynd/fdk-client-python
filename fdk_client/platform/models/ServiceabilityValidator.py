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
        
        page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        name = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
        
        channel_ids = fields.Str(required=False)
        
        q = fields.Str(required=False)
         
    
    class getCompanyStoreView(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updateZoneControllerView(BaseSchema):
        
        zone_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class getZoneDataView(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
         
    
    class createZone(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getZoneFromPincodeView(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class getZonesFromApplicationIdView(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        zone_id = fields.List(fields.Str(required=False), required=False)
        
        q = fields.Str(required=False)
         
    
    class getStore(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        store_uid = fields.Int(required=False)
         
    
    class getAllStores(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updatePincodeMopView(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updatePincodeBulkView(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updatePincodeCoDListing(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class updatePincodeAuditHistory(BaseSchema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    