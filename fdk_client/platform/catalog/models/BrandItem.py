"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Media import Media



from .Action import Action



from .ImageUrls import ImageUrls









class BrandItem(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
