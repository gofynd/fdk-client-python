"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .Action import Action





from .ImageUrls import ImageUrls



from .Media import Media



class BrandItem(BaseSchema):
    #  swagger.json

    
    departments = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    logo = fields.Nested(Media, required=False)
    
