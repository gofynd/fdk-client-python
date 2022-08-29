"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .BrandBannerSerializer import BrandBannerSerializer



















from .BrandDocumentsSerializer import BrandDocumentsSerializer






class GetBrandResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    mode = fields.Str(required=False)
    
    brand_owner = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    owner_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(BrandDocumentsSerializer, required=False), required=False)
    
    slug_key = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    

