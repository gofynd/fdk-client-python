"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .AttributeSchemaRange import AttributeSchemaRange









class AttributeMaster(BaseSchema):
    #  swagger.json

    
    allowed_values = fields.List(fields.Str(required=False), required=False)
    
    multi = fields.Boolean(required=False)
    
    range = fields.Nested(AttributeSchemaRange, required=False)
    
    format = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    mandatory = fields.Boolean(required=False)
    
