"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OptinCompanyMetrics(BaseSchema):
    #  swagger.json

    
    store = fields.Int(required=False)
    
    brand = fields.Int(required=False)
    
    company = fields.Str(required=False)
    