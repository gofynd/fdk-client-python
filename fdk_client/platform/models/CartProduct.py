"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CategoryInfo import CategoryInfo





from .Tags import Tags









from .ProductImage import ProductImage

from .ProductAction import ProductAction

from .BaseInfo import BaseInfo




class CartProduct(BaseSchema):
    # Cart swagger.json

    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    teaser_tag = fields.Nested(Tags, required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    _custom_json = fields.Dict(required=False)
    

