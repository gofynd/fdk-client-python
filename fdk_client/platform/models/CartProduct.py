"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Tags import Tags

from .BaseInfo import BaseInfo





from .ProductImage import ProductImage







from .CategoryInfo import CategoryInfo

from .ProductAction import ProductAction




class CartProduct(BaseSchema):
    # Cart swagger.json

    
    teaser_tag = fields.Nested(Tags, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    

