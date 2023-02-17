"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Action import Action



from .Child import Child







from .ImageUrls import ImageUrls



class CategoryItems(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    action = fields.Nested(Action, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
