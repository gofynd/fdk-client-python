"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductImage import ProductImage

from .BaseInfo import BaseInfo





from .CategoryInfo import CategoryInfo

from .ProductAction import ProductAction






class CartProduct(BaseSchema):
    # Cart swagger.json

    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    

