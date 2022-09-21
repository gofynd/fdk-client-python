"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ThirdLevelChild import ThirdLevelChild





from .ImageUrls import ImageUrls





from .ProductListingAction import ProductListingAction


class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

