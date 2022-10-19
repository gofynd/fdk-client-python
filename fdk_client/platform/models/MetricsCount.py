"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Options import Options


class MetricsCount(BaseSchema):
    # Orders swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    options = fields.List(fields.Nested(Options, required=False), required=False)
    

