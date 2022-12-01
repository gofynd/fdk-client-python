"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .SEOImage import SEOImage





class SEO(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    image = fields.Nested(SEOImage, required=False)
    
    title = fields.Str(required=False)
    
