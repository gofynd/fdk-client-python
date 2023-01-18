"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .ImageUrls import ImageUrls



from .Media import Media



class BrandDetailResponse(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    logo = fields.Nested(Media, required=False)
    
