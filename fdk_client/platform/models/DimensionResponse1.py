"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class DimensionResponse1(BaseSchema):
    # Catalog swagger.json

    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
