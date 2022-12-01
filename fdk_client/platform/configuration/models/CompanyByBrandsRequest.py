"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CompanyByBrandsRequest(BaseSchema):
    #  swagger.json

    
    brands = fields.Int(required=False)
    
    search_text = fields.Str(required=False)
    
