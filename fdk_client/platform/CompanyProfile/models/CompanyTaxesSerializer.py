"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CompanyTaxesSerializer(BaseSchema):
    #  swagger.json

    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    enable = fields.Boolean(required=False)
    
