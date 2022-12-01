"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ThirdLevelChild import ThirdLevelChild



from .ImageUrls import ImageUrls











from .Action import Action



class SecondLevelChild(BaseSchema):
    #  swagger.json

    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
