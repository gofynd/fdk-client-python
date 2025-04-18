"""Configuration Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PublicModel import BaseSchema




class ApplicationResponse(BaseSchema):
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


class SecureUrl(BaseSchema):
    pass


class Application(BaseSchema):
    pass


class TokenSchema(BaseSchema):
    pass


class LocationDefaultLanguage(BaseSchema):
    pass


class LocationDefaultCurrency(BaseSchema):
    pass


class LocationCountry(BaseSchema):
    pass


class Locations(BaseSchema):
    pass


class VersionApplication(BaseSchema):
    pass


class VersionDeviceOS(BaseSchema):
    pass


class VersionDevice(BaseSchema):
    pass


class VersionRequest(BaseSchema):
    pass


class VersionUpdateDialogue(BaseSchema):
    pass


class VersionResponse(BaseSchema):
    pass





class ApplicationResponse(BaseSchema):
    # Configuration swagger.json

    
    application = fields.Nested(Application, required=False)
    


class Domain(BaseSchema):
    # Configuration swagger.json

    
    verified = fields.Boolean(required=False)
    
    is_primary = fields.Boolean(required=False)
    
    is_shortlink = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_predefined = fields.Boolean(required=False)
    


class ApplicationWebsite(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    basepath = fields.Str(required=False)
    


class ApplicationCors(BaseSchema):
    # Configuration swagger.json

    
    domains = fields.List(fields.Str(required=False), required=False)
    


class ApplicationAuth(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class ApplicationRedirections(BaseSchema):
    # Configuration swagger.json

    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationMeta(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SecureUrl(BaseSchema):
    # Configuration swagger.json

    
    secure_url = fields.Str(required=False)
    


class Application(BaseSchema):
    # Configuration swagger.json

    
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
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    banner = fields.Nested(SecureUrl, required=False)
    
    logo = fields.Nested(SecureUrl, required=False)
    
    favicon = fields.Nested(SecureUrl, required=False)
    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    
    app_type = fields.Str(required=False)
    
    mobile_logo = fields.Nested(SecureUrl, required=False)
    
    domain = fields.Nested(Domain, required=False)
    
    slug = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    tokens = fields.List(fields.Nested(TokenSchema, required=False), required=False)
    


class TokenSchema(BaseSchema):
    # Configuration swagger.json

    
    token = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_at = fields.Str(required=False)
    


class LocationDefaultLanguage(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LocationDefaultCurrency(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LocationCountry(BaseSchema):
    # Configuration swagger.json

    
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
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(LocationCountry, required=False), required=False)
    


class VersionApplication(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class VersionDeviceOS(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    


class VersionDevice(BaseSchema):
    # Configuration swagger.json

    
    os = fields.Nested(VersionDeviceOS, required=False)
    


class VersionRequest(BaseSchema):
    # Configuration swagger.json

    
    application = fields.Nested(VersionApplication, required=False)
    
    device = fields.Nested(VersionDevice, required=False)
    


class VersionUpdateDialogue(BaseSchema):
    # Configuration swagger.json

    
    type = fields.Str(required=False)
    
    interval = fields.Int(required=False)
    


class VersionResponse(BaseSchema):
    # Configuration swagger.json

    
    type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    update_dialog = fields.Nested(VersionUpdateDialogue, required=False)
    
    is_app_blocked = fields.Boolean(required=False)
    


