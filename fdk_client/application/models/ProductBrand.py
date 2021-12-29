"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Media import Media





from .ActionPage import ActionPage


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    

