

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
        
        extension_id = fields.Str(required=False, allow_none=True)
        
        scheme_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
        
        status = fields.Str(required=False, allow_none=True)
        
        country = fields.Str(required=False)
        
        region = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class createDeliveryTime(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getDeliveryTimes(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        from_country_code = fields.Str(required=False)
        
        from_state_code = fields.Str(required=False)
        
        from_city_code = fields.Str(required=False)
        
        from_sector_code = fields.Str(required=False)
        
        from_pincode = fields.Str(required=False)
        
        to_country_code = fields.Str(required=False)
        
        to_state_code = fields.Str(required=False)
        
        to_city_code = fields.Str(required=False)
        
        to_sector_code = fields.Str(required=False)
        
        to_pincode = fields.Str(required=False)
         
        
    
    class getDeliveryTime(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateDeliveryTime(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteDeliveryTime(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class createServiceability(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getServiceabilities(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        country_code = fields.Str(required=False)
        
        state_code = fields.Str(required=False)
        
        city_code = fields.Str(required=False)
        
        sector_code = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        first_mile = fields.Boolean(required=False)
        
        last_mile = fields.Boolean(required=False)
        
        doorstep_return = fields.Boolean(required=False)
        
        doorstep_qc = fields.Boolean(required=False)
        
        installation = fields.Boolean(required=False)
         
        
    
    class getServiceability(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateServiceability(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteServiceability(BaseSchema):
        
        
        partner_org_id = fields.Str(required=False)
        
        courier_partner_extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
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
        
        status = fields.Str(required=False, allow_none=True)
        
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
        
        self_ship = fields.Boolean(required=False)
        
        own_account = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class updateCourierPartnerAccount(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        account_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerAccount(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        account_id = fields.Str(required=False)
         
        
    
    class getCountries(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        onboard = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        hierarchy = fields.Str(required=False)
         
        
    
    class createCourierPartnerScheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerSchemes(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        scheme_type = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        capabilities = fields.List(fields.Str(required=False), required=False)
        
        scheme_ids = fields.List(fields.Str(required=False), required=False)
         
        
    
    class updateCourierPartnerScheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getCourierPartnerScheme(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getSampleFileRateCard(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class bulkRateCard(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getBulkRateCard(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
        
        status = fields.Str(required=False, allow_none=True)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class getSampleFileRateZone(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
         
        
    
    class createRateZoneBulkJob(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class getBulkRateZoneJobHistory(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        zone_type = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
         
        
    
    class getRateZoneConfig(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    class updateRateZoneConfiguration(BaseSchema):
        
        
        organization_id = fields.Str(required=False)
        
        extension_id = fields.Str(required=False)
        
        scheme_id = fields.Str(required=False)
         
        
    
    

