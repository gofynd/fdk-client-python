"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CompanyTaxesSerializer import CompanyTaxesSerializer











from .BusinessCountryInfo import BusinessCountryInfo









from .Document import Document



from .GetAddressSerializer import GetAddressSerializer



from .ContactDetails import ContactDetails







from .BusinessDetails import BusinessDetails


class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    sell_gst_exempted_products = fields.Boolean(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    annual_turnover = fields.Str(required=False)
    
    business_type_name = fields.Str(required=False)
    
    about_business = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    mode = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    suppressions = fields.List(fields.Dict(required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    store_name = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    

