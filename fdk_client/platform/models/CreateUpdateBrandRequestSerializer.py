"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .BrandBannerSerializer import BrandBannerSerializer















from .BrandDocumentSerializer import BrandDocumentSerializer


class CreateUpdateBrandRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    brand_tier = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(BrandDocumentSerializer, required=False), required=False)
    

