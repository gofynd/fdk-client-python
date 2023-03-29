"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ItemBrand import ItemBrand
















class Item(BaseSchema):
    # Order swagger.json

    
    brand = fields.Nested(ItemBrand, required=False)
    
    size = fields.Str(required=False)
    
    id = fields.Float(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    slug_key = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

