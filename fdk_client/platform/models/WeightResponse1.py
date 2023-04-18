"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class WeightResponse1(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    shipping = fields.Float(required=False)
    
