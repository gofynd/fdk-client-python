"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Media import Media





from .ImageUrls import ImageUrls



from .Action import Action





class BrandItem(BaseSchema):
    #  swagger.json

    
    discount = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    