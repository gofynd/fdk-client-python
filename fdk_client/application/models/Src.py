"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Src(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    

