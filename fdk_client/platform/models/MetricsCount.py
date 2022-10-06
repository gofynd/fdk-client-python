"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Options import Options






class MetricsCount(BaseSchema):
    # Orders swagger.json

    
    value = fields.Int(required=False)
    
    options = fields.List(fields.Nested(Options, required=False), required=False)
    
    text = fields.Str(required=False)
    
    key = fields.Str(required=False)
    

