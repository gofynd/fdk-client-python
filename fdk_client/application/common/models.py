"""Common Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class ApplicationResponseSchema(BaseSchema):
    pass


class Domain(BaseSchema):
    pass


class ApplicationWebsite(BaseSchema):
    pass


class ApplicationCors(BaseSchema):
    pass


class ApplicationAuth(BaseSchema):
    pass


class ApplicationRedirections(BaseSchema):
    pass


class ApplicationMeta(BaseSchema):
    pass


class RegionDetails(BaseSchema):
    pass


class SecureUrl(BaseSchema):
    pass


class Application(BaseSchema):
    pass


class NotFound(BaseSchema):
    pass


class BadRequestSchema(BaseSchema):
    pass


class LocationDefaultLanguage(BaseSchema):
    pass


class LocationDefaultCurrency(BaseSchema):
    pass


class LocationCountry(BaseSchema):
    pass


class Locations(BaseSchema):
    pass





class ApplicationResponseSchema(BaseSchema):
    # Common swagger.json

    
    application = fields.Nested(Application, required=False)
    


class Domain(BaseSchema):
    # Common swagger.json

    
    verified = fields.Boolean(required=False)
    
    is_primary = fields.Boolean(required=False)
    
    is_shortlink = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_predefined = fields.Boolean(required=False)
    


class ApplicationWebsite(BaseSchema):
    # Common swagger.json

    
    enabled = fields.Boolean(required=False)
    
    basepath = fields.Str(required=False)
    


class ApplicationCors(BaseSchema):
    # Common swagger.json

    
    domains = fields.List(fields.Str(required=False), required=False)
    


class ApplicationAuth(BaseSchema):
    # Common swagger.json

    
    enabled = fields.Boolean(required=False)
    


class ApplicationRedirections(BaseSchema):
    # Common swagger.json

    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationMeta(BaseSchema):
    # Common swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class RegionDetails(BaseSchema):
    # Common swagger.json

    
    slug = fields.Str(required=False)
    
    zone = fields.Str(required=False)
    


class SecureUrl(BaseSchema):
    # Common swagger.json

    
    secure_url = fields.Str(required=False)
    


class Application(BaseSchema):
    # Common swagger.json

    
    website = fields.Nested(ApplicationWebsite, required=False)
    
    cors = fields.Nested(ApplicationCors, required=False)
    
    auth = fields.Nested(ApplicationAuth, required=False)
    
    description = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    cache_ttl = fields.Int(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    owner = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    token = fields.Str(required=False)
    
    redirections = fields.List(fields.Nested(ApplicationRedirections, required=False), required=False)
    
    meta = fields.List(fields.Nested(ApplicationMeta, required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    banner = fields.Nested(SecureUrl, required=False)
    
    logo = fields.Nested(SecureUrl, required=False)
    
    favicon = fields.Nested(SecureUrl, required=False)
    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    
    app_type = fields.Str(required=False)
    
    mobile_logo = fields.Nested(SecureUrl, required=False)
    
    domain = fields.Nested(Domain, required=False)
    


class NotFound(BaseSchema):
    # Common swagger.json

    
    message = fields.Str(required=False)
    


class BadRequestSchema(BaseSchema):
    # Common swagger.json

    
    message = fields.Str(required=False)
    


class LocationDefaultLanguage(BaseSchema):
    # Common swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LocationDefaultCurrency(BaseSchema):
    # Common swagger.json

    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LocationCountry(BaseSchema):
    # Common swagger.json

    
    capital = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    parent = fields.Str(required=False)
    
    phone_code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    __v = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    default_currency = fields.Nested(LocationDefaultCurrency, required=False)
    
    default_language = fields.Nested(LocationDefaultLanguage, required=False)
    
    state_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class Locations(BaseSchema):
    # Common swagger.json

    
    items = fields.List(fields.Nested(LocationCountry, required=False), required=False)
    


