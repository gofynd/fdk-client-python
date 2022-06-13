"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductListingAction import ProductListingAction



from .ImageUrls import ImageUrls

from .SecondLevelChild import SecondLevelChild




class Child(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    

