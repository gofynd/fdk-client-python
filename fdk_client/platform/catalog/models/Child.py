"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ImageUrls import ImageUrls









from .SecondLevelChild import SecondLevelChild



from .Action import Action





class Child(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    _custom_json = fields.Dict(required=False)
    
