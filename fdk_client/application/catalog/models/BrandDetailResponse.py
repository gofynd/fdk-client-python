"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Media import Media





from .ImageUrls import ImageUrls







class BrandDetailResponse(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
