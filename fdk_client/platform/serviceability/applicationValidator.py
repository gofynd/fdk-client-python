

"""Serviceability Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        

class ServiceabilityValidator:
    
    
    class createZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getZones(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        access_level = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        country_iso_code = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        sector = fields.Str(required=False)
         
        
    
    class getZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class deleteZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getZoneDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        zone_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createBulkZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getBulkZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createBulkExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getBulkExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class updatePincodeMopView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updatePincodeBulkView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updatePincodeCoDListing(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updatePincodeAuditHistory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createGeoArea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getGeoAreas(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        type = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        country_iso_code = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        sector = fields.Str(required=False)
         
        
    
    class getGeoArea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        geoarea_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateGeoArea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        geoarea_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createBulkGeoArea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getBulkGeoArea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        geoarea_id = fields.Str(required=False)
         
        
    
    class updateBulkGeoArea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        geoarea_id = fields.Str(required=False)
         
        
    
    class createGeoAreaExportJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        geoarea_id = fields.Str(required=False)
         
        
    
    class getGeoAreaExportJobStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        geoarea_id = fields.Str(required=False)
         
        
    
    class createBulkGeoAreaExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createBulkGeoAreas(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class validateBulkGeoarea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getBulkGeoareaValidation(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class importBulkGeoarea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class importBulkGeoareaStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class overrideBulkGeoarea(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class getGeoareaOverrideStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class getBulkGeoAreasHistory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getBulkGeoAreasSample(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getGeoAreasExportStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class createCourierPartnerRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        status = fields.Str(required=False)
         
        
    
    class updateCourierRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class getCourierPartnerRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class updateApplicationConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getApplicationConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class patchApplicationConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getApplicationConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class insertApplicationConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateStoreRulesConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getStoreRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        status = fields.Str(required=False)
         
        
    
    class createStoreRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateStoreRulePriority(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getStoreRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class updateStoreRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class updateCourierPartnerRulePriority(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerRuleDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class getStoreRuleDetails(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class downloadGeoareaSampleFile(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class downloadZoneSampleFile(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        product_type = fields.Str(required=False)
         
        
    
    class validateBulkZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getBulkZoneValidation(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class importBulkZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class overrideZoneById(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        zone_id = fields.Str(required=False)
         
        
    
    class getZoneOverrideStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        zone_id = fields.Str(required=False)
         
        
    
    class overrideBulkZone(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class getBulkZoneOverrideStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    

