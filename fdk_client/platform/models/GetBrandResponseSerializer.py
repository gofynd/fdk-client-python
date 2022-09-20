"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema























from .BrandDocumentsSerializer import BrandDocumentsSerializer





from .BrandBannerSerializer import BrandBannerSerializer






class GetBrandResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    mode = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    corrections = fields.List(fields.Dict(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(BrandDocumentsSerializer, required=False), required=False)
    
    brand_owner = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    slug_key = fields.Str(required=False)
    
    owner_id = fields.Int(required=False)
    

