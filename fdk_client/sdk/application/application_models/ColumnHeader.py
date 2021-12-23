"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ColumnHeader(BaseSchema):
    # Catalog swagger.json

    
    convertable = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    

