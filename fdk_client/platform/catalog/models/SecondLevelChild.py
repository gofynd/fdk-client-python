"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ThirdLevelChild import ThirdLevelChild



from .ImageUrls import ImageUrls









from .Action import Action



class SecondLevelChild(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
