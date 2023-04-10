"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TATCategoryRequest(BaseSchema):
    # Logistic swagger.json

    
    level = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

