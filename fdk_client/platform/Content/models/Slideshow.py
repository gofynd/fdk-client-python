"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SlideshowSchema import SlideshowSchema





class Slideshow(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(SlideshowSchema, required=False)
    
    success = fields.Boolean(required=False)
    
