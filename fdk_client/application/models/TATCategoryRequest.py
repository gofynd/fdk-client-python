"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TATCategoryRequest(BaseSchema):
    # Logistic swagger.json

    
    id = fields.Str(required=False)
    
    level = fields.Str(required=False)
    

