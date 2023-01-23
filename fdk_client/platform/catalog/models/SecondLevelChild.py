"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ImageUrls import ImageUrls









from .Action import Action





from .ThirdLevelChild import ThirdLevelChild



class SecondLevelChild(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(Action, required=False)
    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
