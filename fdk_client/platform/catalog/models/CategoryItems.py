"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Action import Action



from .ImageUrls import ImageUrls





from .Child import Child





class CategoryItems(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    slug = fields.Str(required=False)
    
