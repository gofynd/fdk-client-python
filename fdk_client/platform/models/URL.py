"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class URL(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    

