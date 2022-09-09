"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductListingAction import ProductListingAction





from .ImageUrls import ImageUrls




class ThirdLevelChild(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    

