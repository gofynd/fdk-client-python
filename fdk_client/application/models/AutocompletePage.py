"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PageQuery import PageQuery




class AutocompletePage(BaseSchema):
    # Catalog swagger.json

    
    query = fields.Nested(PageQuery, required=False)
    
    type = fields.Str(required=False)
    

