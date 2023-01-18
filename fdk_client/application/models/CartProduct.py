"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Tags import Tags





from .BaseInfo import BaseInfo

from .ProductAction import ProductAction

from .CategoryInfo import CategoryInfo







from .ProductImage import ProductImage




class CartProduct(BaseSchema):
    # Cart swagger.json

    
    teaser_tag = fields.Nested(Tags, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    uid = fields.Int(required=False)
    

