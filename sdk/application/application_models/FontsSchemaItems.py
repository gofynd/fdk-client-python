"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema











from .FontsSchemaItemsFiles import FontsSchemaItemsFiles






class FontsSchemaItems(BaseSchema):

    
    family = fields.Str(required=False)
    
    variants = fields.List(fields.Str(required=False), required=False)
    
    subsets = fields.List(fields.Str(required=False), required=False)
    
    version = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    files = fields.Nested(FontsSchemaItemsFiles, required=False)
    
    category = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    

