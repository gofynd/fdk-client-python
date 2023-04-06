"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Dimensions(BaseSchema):
    # Order swagger.json

    
    unit = fields.Str(required=False)
    
    length = fields.Int(required=False)
    
    height = fields.Int(required=False)
    
    width = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    

