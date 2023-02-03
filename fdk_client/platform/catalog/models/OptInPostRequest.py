"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class OptInPostRequest(BaseSchema):
    #  swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    platform = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    opt_level = fields.Str(required=False)
    
