"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .BrandBannerSerializer import BrandBannerSerializer



















class CreateUpdateBrandRequestSerializer(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    brand_tier = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
