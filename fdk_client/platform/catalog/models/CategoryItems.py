"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Child import Child



from .Action import Action



from .ImageUrls import ImageUrls









class CategoryItems(BaseSchema):
    #  swagger.json

    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
