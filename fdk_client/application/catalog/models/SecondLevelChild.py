"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductListingAction import ProductListingAction



from .ImageUrls import ImageUrls









from .ThirdLevelChild import ThirdLevelChild



class SecondLevelChild(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
