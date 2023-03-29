"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .FilterInfoOption import FilterInfoOption


class FiltersInfo(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(FilterInfoOption, required=False), required=False)
    

