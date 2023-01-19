"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .TaxSlab import TaxSlab











class HSNDataInsertV2(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(TaxSlab, required=False), required=False)
    
    country_code = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    reporting_hsn = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
