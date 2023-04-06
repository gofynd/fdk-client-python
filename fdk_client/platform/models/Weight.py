"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Weight(BaseSchema):
    # Order swagger.json

    
    unit = fields.Str(required=False)
    
    shipping = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    

