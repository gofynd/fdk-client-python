"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CompanyBrandPostRequestSerializer(BaseSchema):
    #  swagger.json

    
    company = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
