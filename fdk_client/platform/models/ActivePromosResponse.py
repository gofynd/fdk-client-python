"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class ActivePromosResponse(BaseSchema):
    # Cart swagger.json

    
    is_hidden = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    entity_slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    example = fields.Str(required=False)
    

