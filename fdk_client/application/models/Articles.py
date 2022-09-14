"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Category import Category






class Articles(BaseSchema):
    # Logistic swagger.json

    
    category = fields.Nested(Category, required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    

