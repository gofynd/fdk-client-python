"""Catalog Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema




class Page(BaseSchema):
    pass


class CompanyListSchema(BaseSchema):
    pass


class CompaniesSchema(BaseSchema):
    pass


class ErrorResponseSchema(BaseSchema):
    pass


class PartnerCompanyDetailsRequestSchema(BaseSchema):
    pass


class CompanySchema(BaseSchema):
    pass


class GetAddressSchema(BaseSchema):
    pass


class BusinessCountryInfo(BaseSchema):
    pass


class CountryCurrencyInfo(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class CompanyDetails(BaseSchema):
    pass


class CompanySocialAccounts(BaseSchema):
    pass





class Page(BaseSchema):
    # Catalog swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class CompanyListSchema(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(CompanySchema, required=False), required=False)
    


class CompaniesSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CompanySchema, required=False), required=False)
    


class ErrorResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    


class PartnerCompanyDetailsRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    company_ids = fields.List(fields.Int(required=False), required=False)
    


class CompanySchema(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSchema, required=False), required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    reject_reason = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    


class GetAddressSchema(BaseSchema):
    # Catalog swagger.json

    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    pincode = fields.Str(required=False)
    
    state = fields.Str(required=False)
    


class BusinessCountryInfo(BaseSchema):
    # Catalog swagger.json

    
    country_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    currency = fields.Nested(CountryCurrencyInfo, required=False)
    
    timezone = fields.Str(required=False)
    


class CountryCurrencyInfo(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class UserSchema(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class CompanyDetails(BaseSchema):
    # Catalog swagger.json

    
    socials = fields.List(fields.Nested(CompanySocialAccounts, required=False), required=False)
    
    website_url = fields.Str(required=False)
    


class CompanySocialAccounts(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


