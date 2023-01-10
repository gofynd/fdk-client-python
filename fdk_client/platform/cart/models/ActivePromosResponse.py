"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class ActivePromosResponse(BaseSchema):
    #  swagger.json

    
    created_on = fields.Str(required=False)
    
    example = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    entity_slug = fields.Str(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
