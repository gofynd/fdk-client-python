"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class FontsSchemaItemsFiles(BaseSchema):

    
    regular = fields.Str(required=False)
    
    italic = fields.Str(required=False)
    
    bold = fields.Str(required=False)
    

