"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Formatted(BaseSchema):
    # Orders swagger.json

    
    f_max = fields.Str(required=False)
    
    f_min = fields.Str(required=False)
    

