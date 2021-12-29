"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class LocationDefaultLanguage(BaseSchema):
    # Common swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

