"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductListingAction import ProductListingAction





from .SecondLevelChild import SecondLevelChild



from .ImageUrls import ImageUrls



class Child(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    name = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
