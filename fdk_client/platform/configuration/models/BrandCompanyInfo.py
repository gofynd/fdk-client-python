"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BrandCompanyInfo(BaseSchema):
    #  swagger.json

    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
