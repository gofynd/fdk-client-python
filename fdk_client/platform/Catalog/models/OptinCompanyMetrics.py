"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OptinCompanyMetrics(BaseSchema):
    #  swagger.json

    
    company = fields.Str(required=False)
    
    brand = fields.Int(required=False)
    
    store = fields.Int(required=False)
    
