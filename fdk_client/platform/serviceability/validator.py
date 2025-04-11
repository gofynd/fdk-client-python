

"""Serviceability Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
    
    
        
    
    
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
    
    
        
        
        
        
        
        
    
    
        
    
    
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
    
    
        



class ServiceabilityValidator:
    
    
    class updateCompanySelfShip(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCompanySelfShip(BaseSchema):
        
        
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
        
        account_ids = fields.List(fields.Str(required=False), required=False)
        
        self_ship = fields.Boolean(required=False)
        
        own_account = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
         
        
    
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
         
        
    
    class createPackageMaterial(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    class getPackageMaterialList(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        package_type = fields.Str(required=False)
         
        
    
    class createPackageMaterialRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getPackageMaterialRuleDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_active = fields.Str(required=False)
         
        
    
    class getListPackageMaterialRuleDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_active = fields.Str(required=False)
         
        
    
    class getPackageMaterialRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_id = fields.Str(required=False)
         
        
    
    class updatePackageMaterialRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_id = fields.Str(required=False)
         
        
    
    class deletePackageMaterialRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        rule_id = fields.Str(required=False)
         
        
    
    class updatePackageMaterials(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        package_material_id = fields.Str(required=False)
         
        
    
    class getPackageMaterials(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        package_material_id = fields.Str(required=False)
         
        
    
    class deletePackageMaterials(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        package_material_id = fields.Str(required=False)
         
        
    
    class getInstalledCourierPartnerExtensions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_installed = fields.Str(required=False)
         
        
    
    class getLocalitiesByPrefix(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getLocality(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        locality_type = fields.Str(required=False)
        
        locality_value = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
         
        
    
    class getLocalities(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        locality_type = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        name = fields.Str(required=False)
         
        
    
    class getCountry(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        country_iso_code = fields.Str(required=False)
         
        
    
    class getCountries(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        onboard = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        hierarchy = fields.Str(required=False)
         
        
    
    class validateAddress(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        country_iso_code = fields.Str(required=False)
        
        template_name = fields.Str(required=False)
         
        
    
    class getOptimalLocations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    

