

"""Serviceability Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
        
        
        
        
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
    
    
        
        
        
        
        
        
    
    
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        



class ServiceabilityValidator:
    
    
    class getZones(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        channel_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        country_iso_code = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        sector = fields.Str(required=False)
         
        
    
    class createZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class updateZoneById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
         
        
    
    class getZoneById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
         
        
    
    class getAllStores(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class createCourierPartnerAccount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCourierPartnerAccounts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        stage = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        transport_type = fields.Str(required=False)
         
        
    
    class updateCourierPartnerAccount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        account_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerAccount(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        account_id = fields.Str(required=False)
         
        
    
    class updateCompanyConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCompanyConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class bulkTat(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getBulkTat(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
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
        
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getBulkServiceability(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
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
         
        
    
    class getServiceability(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        region_id = fields.Str(required=False)
         
        
    
    class updateServiceability(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        region_id = fields.Str(required=False)
         
        
    
    class createPackageMaterial(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getPackageMaterialList(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        package_type = fields.Str(required=False)
         
        
    
    class createPackageMaterialRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getPackageMaterialRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_active = fields.Str(required=False)
         
        
    
    class updatePackageMaterialRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_id = fields.Str(required=False)
         
        
    
    class getPackageMaterialRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_id = fields.Str(required=False)
         
        
    
    class updatePackageMaterials(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        package_material_id = fields.Str(required=False)
         
        
    
    class getPackageMaterials(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        package_material_id = fields.Str(required=False)
         
        
    
    class getOptimalLocations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class createCourierPartnerScheme(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCourierPartnerSchemes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        scheme_type = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        capabilities = fields.List(fields.Str(required=False), required=False)
        
        scheme_ids = fields.List(fields.Str(required=False), required=False)
         
        
    
    class updateCourierPartnerScheme(BaseSchema):
        
        
        scheme_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getCourierPartnerScheme(BaseSchema):
        
        
        scheme_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class sampleFileServiceability(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getSampleFileServiceabilityStatus(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getCountries(BaseSchema):
        
        
        onboarding = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        hierarchy = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    

