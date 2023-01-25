"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ImageUrls import ImageUrls





from .ThirdLevelChild import ThirdLevelChild



from .Action import Action





class SecondLevelChild(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
