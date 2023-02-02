"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ImageUrls import ImageUrls





from .ProductListingAction import ProductListingAction









class ThirdLevelChild(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
