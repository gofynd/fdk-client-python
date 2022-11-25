"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSerializer import UserSerializer



from .BusinessDetails import BusinessDetails





from .GetAddressSerializer import GetAddressSerializer



from .CompanyTaxesSerializer import CompanyTaxesSerializer





from .UserSerializer import UserSerializer









from .Document import Document











from .UserSerializer import UserSerializer



from .ContactDetails import ContactDetails





from .BusinessCountryInfo import BusinessCountryInfo









class GetCompanyProfileSerializerResponse(BaseSchema):
    #  swagger.json

    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    business_info = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    business_type = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    warnings = fields.Dict(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    name = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    mode = fields.Str(required=False)
    
