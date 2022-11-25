"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CompanyTaxesSerializer(BaseSchema):
    #  swagger.json

    
    rate = fields.Float(required=False)
    
    enable = fields.Boolean(required=False)
    
    effective_date = fields.Str(required=False)
    
