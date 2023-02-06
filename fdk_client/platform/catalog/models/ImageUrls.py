"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BannerImage import BannerImage



from .BannerImage import BannerImage



class ImageUrls(BaseSchema):
    #  swagger.json

    
    landscape = fields.Nested(BannerImage, required=False)
    
    portrait = fields.Nested(BannerImage, required=False)
    
