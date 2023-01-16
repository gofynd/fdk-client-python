"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class SizeGuideResponse(BaseSchema):
    #  swagger.json

    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    tag = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    guide = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    