"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Child import Child





from .ImageUrls import ImageUrls



from .Action import Action



class CategoryItems(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(Action, required=False)
    