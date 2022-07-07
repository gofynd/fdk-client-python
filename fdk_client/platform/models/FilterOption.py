"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class FilterOption(BaseSchema):
    # Orders swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

