"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Action import Action



from .Media import Media



from .ImageUrls import ImageUrls









class BrandItem(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
