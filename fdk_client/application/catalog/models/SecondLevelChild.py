"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ImageUrls import ImageUrls







from .ProductListingAction import ProductListingAction





from .ThirdLevelChild import ThirdLevelChild



class SecondLevelChild(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
