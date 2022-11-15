"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class TaxIdentifier(BaseSchema):
    #  swagger.json

    
    reporting_hsn = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
