"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BannerImage import BannerImage



from .BannerImage import BannerImage



class ImageUrls(BaseSchema):
    #  swagger.json

    
    portrait = fields.Nested(BannerImage, required=False)
    
    landscape = fields.Nested(BannerImage, required=False)
    
