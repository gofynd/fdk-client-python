"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BusinessCountryInfo import BusinessCountryInfo









from .CompanyDetails import CompanyDetails

from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer

from .GetAddressSerializer import GetAddressSerializer







from .UserSerializer import UserSerializer








class CompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    reject_reason = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    stage = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    company_type = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    

