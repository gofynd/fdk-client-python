"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Document import Document







from .UserSerializer import UserSerializer







from .BusinessDetails import BusinessDetails









from .GetAddressSerializer import GetAddressSerializer



from .UserSerializer import UserSerializer

from .BusinessCountryInfo import BusinessCountryInfo



from .ContactDetails import ContactDetails

from .UserSerializer import UserSerializer




class GetCompanyProfileSerializerResponse(BaseSchema):

    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    company_type = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    stage = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    uid = fields.Int(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    

