"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class JsonFields(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Dict(required=False)
    
    key = fields.Str(required=False)
    

