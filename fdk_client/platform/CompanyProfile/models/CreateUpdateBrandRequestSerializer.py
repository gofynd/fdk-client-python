"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















from .BrandBannerSerializer import BrandBannerSerializer



class CreateUpdateBrandRequestSerializer(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    brand_tier = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
