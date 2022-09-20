"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .BusinessCountryInfo import BusinessCountryInfo





from .GetAddressSerializer import GetAddressSerializer







from .CompanyTaxesSerializer import CompanyTaxesSerializer



from .Document import Document

from .BusinessDetails import BusinessDetails



from .ContactDetails import ContactDetails












class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    franchise_enabled = fields.Boolean(required=False)
    
    about_business = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    business_type_name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    company_type = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    annual_turnover = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    mode = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    suppressions = fields.List(fields.Dict(required=False), required=False)
    
    sell_gst_exempted_products = fields.Boolean(required=False)
    
    business_info = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    

