"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class CompanyBrandDetail(BaseSchema):
    #  swagger.json

    
    brand_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    
    total_article = fields.Int(required=False)
    
