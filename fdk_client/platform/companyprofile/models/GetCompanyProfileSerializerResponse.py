"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .BusinessDetails import BusinessDetails





from .ContactDetails import ContactDetails



from .CompanyTaxesSerializer import CompanyTaxesSerializer











from .UserSerializer import UserSerializer











from .BusinessCountryInfo import BusinessCountryInfo



from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer



from .GetAddressSerializer import GetAddressSerializer





from .Document import Document



class GetCompanyProfileSerializerResponse(BaseSchema):
    #  swagger.json

    
    business_type = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    created_on = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    mode = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
