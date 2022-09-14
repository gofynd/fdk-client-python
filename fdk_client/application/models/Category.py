"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Category(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

