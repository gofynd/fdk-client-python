"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SubLane import SubLane




class SuperLane(BaseSchema):
    # Orders swagger.json

    
    value = fields.Str(required=False)
    
    options = fields.List(fields.Nested(SubLane, required=False), required=False)
    
    text = fields.Str(required=False)
    
