"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ValidateIdentifier(BaseSchema):
    # Catalog swagger.json

    
    gtin_value = fields.Str(required=False)
    
    gtin_type = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    

