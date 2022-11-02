"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class OptinCompanyDetail(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    business_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
