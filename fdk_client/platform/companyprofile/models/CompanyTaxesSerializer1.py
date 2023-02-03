"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CompanyTaxesSerializer1(BaseSchema):
    #  swagger.json

    
    enable = fields.Boolean(required=False)
    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
