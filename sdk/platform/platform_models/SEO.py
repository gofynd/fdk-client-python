"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .SEOImage import SEOImage




class SEO(BaseSchema):

    
    description = fields.Str(required=False)
    
    image = fields.Nested(SEOImage, required=False)
    
    title = fields.Str(required=False)
    

