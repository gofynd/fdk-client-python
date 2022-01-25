"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PageQuery(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.List(fields.Str(required=False), required=False)
    
    category = fields.List(fields.Str(required=False), required=False)
    

