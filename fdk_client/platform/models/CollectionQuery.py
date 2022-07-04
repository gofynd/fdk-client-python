"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CollectionQuery(BaseSchema):
    # Catalog swagger.json

    
    value = fields.List(fields.Str(required=False), required=False)
    
    op = fields.Str(required=False)
    
    attribute = fields.Str(required=False)
    

