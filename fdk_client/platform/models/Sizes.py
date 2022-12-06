"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Sizes(BaseSchema):
    # Order swagger.json

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    
