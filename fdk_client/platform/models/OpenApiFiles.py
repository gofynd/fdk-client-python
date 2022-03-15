"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OpenApiFiles(BaseSchema):
    # Cart swagger.json

    
    values = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    

