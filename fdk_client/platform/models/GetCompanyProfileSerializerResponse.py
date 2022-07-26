"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Document import Document







from .UserSerializer import UserSerializer







from .UserSerializer import UserSerializer





from .GetAddressSerializer import GetAddressSerializer







from .ContactDetails import ContactDetails



from .CompanyTaxesSerializer import CompanyTaxesSerializer





from .BusinessDetails import BusinessDetails







from .BusinessCountryInfo import BusinessCountryInfo



from .UserSerializer import UserSerializer




class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    sell_gst_exempted_products = fields.Boolean(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    business_type = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    about_business = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    suppressions = fields.List(fields.Dict(required=False), required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    mode = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    annual_turnover = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    

