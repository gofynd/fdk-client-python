"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class BannerImage(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
