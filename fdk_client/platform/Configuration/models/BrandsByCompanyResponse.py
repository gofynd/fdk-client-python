"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CompanyBrandInfo import CompanyBrandInfo



class BrandsByCompanyResponse(BaseSchema):
    #  swagger.json

    
    brands = fields.Nested(CompanyBrandInfo, required=False)
    
