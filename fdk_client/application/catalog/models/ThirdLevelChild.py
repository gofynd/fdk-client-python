"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductListingAction import ProductListingAction



from .ImageUrls import ImageUrls









class ThirdLevelChild(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    slug = fields.Str(required=False)
    
