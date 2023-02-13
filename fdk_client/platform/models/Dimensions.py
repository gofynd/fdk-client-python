"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Dimensions(BaseSchema):
    # Orders swagger.json

    
    length = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    height = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    
    width = fields.Int(required=False)
    
