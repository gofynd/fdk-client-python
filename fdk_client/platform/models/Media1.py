"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Media1(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
