"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Action import Action









from .ImageUrls import ImageUrls







class ThirdLevelChild(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(Action, required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
