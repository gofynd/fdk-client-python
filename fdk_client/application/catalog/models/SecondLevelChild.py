"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ThirdLevelChild import ThirdLevelChild



from .ProductListingAction import ProductListingAction









from .ImageUrls import ImageUrls





class SecondLevelChild(BaseSchema):
    #  swagger.json

    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
