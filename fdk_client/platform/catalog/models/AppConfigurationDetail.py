"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .AttributeDetailsGroup import AttributeDetailsGroup













class AppConfigurationDetail(BaseSchema):
    #  swagger.json

    
    is_default = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    template_slugs = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.List(fields.Nested(AttributeDetailsGroup, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
