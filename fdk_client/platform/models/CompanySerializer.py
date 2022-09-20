"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CompanyDetails import CompanyDetails













from .BusinessCountryInfo import BusinessCountryInfo

from .GetAddressSerializer import GetAddressSerializer


class CompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    business_type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    reject_reason = fields.Str(required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    

