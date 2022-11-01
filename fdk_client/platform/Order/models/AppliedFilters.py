"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class AppliedFilters(BaseSchema):
    #  swagger.json

    
    stage = fields.Str(required=False)
    
    stores = fields.List(fields.Str(required=False), required=False)
    
    deployment_stores = fields.List(fields.Str(required=False), required=False)
    
    dp = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    
