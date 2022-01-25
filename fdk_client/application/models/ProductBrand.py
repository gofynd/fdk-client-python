"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Action import Action





from .Media import Media


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    

