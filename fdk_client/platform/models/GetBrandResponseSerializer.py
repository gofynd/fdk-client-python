"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .BrandBannerSerializer import BrandBannerSerializer

from .UserSerializer import UserSerializer

















from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer






class GetBrandResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    description = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    

