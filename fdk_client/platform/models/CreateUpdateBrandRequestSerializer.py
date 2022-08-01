"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BrandDocumentSerializer import BrandDocumentSerializer



















from .BrandBannerSerializer import BrandBannerSerializer


class CreateUpdateBrandRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.List(fields.Nested(BrandDocumentSerializer, required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    brand_tier = fields.Str(required=False)
    
    document_required = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    

