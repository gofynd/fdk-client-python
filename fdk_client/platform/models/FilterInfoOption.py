"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class FilterInfoOption(BaseSchema):
    # Orders swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    

