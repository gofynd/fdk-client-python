"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSerializer import UserSerializer









from .BrandBannerSerializer import BrandBannerSerializer



















from .UserSerializer import UserSerializer





from .UserSerializer import UserSerializer









class GetBrandResponseSerializer(BaseSchema):
    #  swagger.json

    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
