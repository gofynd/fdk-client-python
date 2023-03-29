"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Dimension(BaseSchema):
    # Catalog swagger.json

    
    is_default = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    

