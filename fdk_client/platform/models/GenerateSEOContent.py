"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class GenerateSEOContent(BaseSchema):
    # Content swagger.json

    
    text = fields.Str(required=False)
    
    existing_text = fields.Str(required=False)
    
    keywords = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    

