

"""Logistics Partner Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema



    
    
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
    
    
        
        
    
    
        
        
        
        
        
        

class LogisticsValidator:
    
    
    class sampleFileServiceability(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class getSampleFileServiceabilityStatus(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class bulkTat(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getBulkTat(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        region = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class bulkServiceability(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getBulkServiceability(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        region = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class createCourierPartnerAccount(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getCourierPartnerAccounts(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        stage = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        transport_type = fields.Str(required=False)
        
        account_ids = fields.List(fields.Str(required=False), required=False)
         
        
    
    class updateCourierPartnerAccount(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        account_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerAccount(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        account_id = fields.Str(required=False)
         
        
    
    class createCourierPartnerScheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class updateCourierPartnerScheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getCountries(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        onboard = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        hierarchy = fields.Str(required=False)
         
        
    
    

