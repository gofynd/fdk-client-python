"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .BrandDocumentSerializer import BrandDocumentSerializer







from .BrandBannerSerializer import BrandBannerSerializer


class CreateUpdateBrandRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    brand_tier = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.List(fields.Nested(BrandDocumentSerializer, required=False), required=False)
    
    description = fields.Str(required=False)
    
    document_required = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    

