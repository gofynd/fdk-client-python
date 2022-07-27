"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class FilterInfoOption(BaseSchema):
    # Orders swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

