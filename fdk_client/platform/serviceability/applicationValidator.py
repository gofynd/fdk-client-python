

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
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        fulfillment_option_slug = fields.Str(required=False)
        
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
         
        
    
    class createBulkExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getBulkExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
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
         
        
    
    class updatePincodeMopView(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updatePincodeBulkView(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updatePincodeCoDListing(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class updatePincodeAuditHistory(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_number = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class updateCourierRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class getCourierPartnerRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        rule_uid = fields.Str(required=False)
         
        
    
    class createCourierPartnerRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        status = fields.Str(required=False)
         
        
    
    class getCourierPartners(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
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
         
        
    
    class updateStoreRulePriority(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class downloadGeoareaSampleFile(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createFulfillmentOption(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getFulfillmentOptionsList(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        product_slug = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
        
        status = fields.Str(required=False)
         
        
    
    class getFulfillmentOptions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
        
        product_id = fields.Int(required=False)
        
        store_id = fields.Int(required=False)
         
        
    
    class deleteFulfillmentOptions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class putFulfillmentOption(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class getFulfillmentOptionProducts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
         
        
    
    class getFulfillmentOptionStores(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class uploadBulkFulfillmentOptions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class validateBulkFulfillmentOptions(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
        
    
    class getBulkFulfillmentValidationStatus(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        bulk_id = fields.Str(required=False)
         
        
    
    

