"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class ProductSortOn(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    

