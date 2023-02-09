"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class CompanyOptIn(BaseSchema):
    #  swagger.json

    
    created_on = fields.Int(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Int(required=False)
    
    opt_level = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    platform = fields.Str(required=False)
    
