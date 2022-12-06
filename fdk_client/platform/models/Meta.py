"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Meta(BaseSchema):
    # Catalog swagger.json

    
    headers = fields.Dict(required=False)
    
    unit = fields.Str(required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    

