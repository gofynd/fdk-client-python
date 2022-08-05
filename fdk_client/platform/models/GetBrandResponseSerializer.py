"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .UserSerializer import UserSerializer





from .BrandBannerSerializer import BrandBannerSerializer





from .BrandDocumentsSerializer import BrandDocumentsSerializer







from .UserSerializer import UserSerializer



















from .UserSerializer import UserSerializer


class GetBrandResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    mode = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    slug_key = fields.Str(required=False)
    
    brand_owner = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(BrandDocumentsSerializer, required=False), required=False)
    
    name = fields.Str(required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    owner_id = fields.Int(required=False)
    
    reject_reason = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    

