"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Media import Media







from .ImageUrls import ImageUrls







from .Action import Action



class BrandItem(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    discount = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
