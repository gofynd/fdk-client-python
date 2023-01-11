"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SecondLevelChild import SecondLevelChild





from .ImageUrls import ImageUrls





from .ProductListingAction import ProductListingAction







class Child(BaseSchema):
    #  swagger.json

    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
