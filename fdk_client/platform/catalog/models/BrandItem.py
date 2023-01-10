"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Action import Action











from .Media import Media





from .ImageUrls import ImageUrls



class BrandItem(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
