"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BusinessCountryInfo import BusinessCountryInfo



from .UserSerializer import UserSerializer





from .GetAddressSerializer import GetAddressSerializer





from .CompanyTaxesSerializer import CompanyTaxesSerializer



from .UserSerializer import UserSerializer









from .ContactDetails import ContactDetails





from .UserSerializer import UserSerializer











from .BusinessDetails import BusinessDetails







from .Document import Document





class GetCompanyProfileSerializerResponse(BaseSchema):
    #  swagger.json

    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    stage = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    business_info = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    business_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    name = fields.Str(required=False)
    
