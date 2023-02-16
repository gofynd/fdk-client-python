"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .Guide import Guide























class ValidateSizeGuide(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    guide = fields.Nested(Guide, required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    subtitle = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
