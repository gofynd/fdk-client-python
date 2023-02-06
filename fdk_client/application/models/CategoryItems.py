"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductListingAction import ProductListingAction

from .CategoryBanner import CategoryBanner

from .Child import Child






class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    banners = fields.Nested(CategoryBanner, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

