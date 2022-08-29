"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .GetAddressSerializer import GetAddressSerializer



from .BusinessCountryInfo import BusinessCountryInfo

from .CompanyDetails import CompanyDetails








class CompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    company_type = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    reject_reason = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    

