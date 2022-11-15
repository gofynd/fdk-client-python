"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .SEO import SEO



from .MOQ import MOQ



class ApplicationItemResponse(BaseSchema):
    #  swagger.json

    
    alt_text = fields.Dict(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    moq = fields.Nested(MOQ, required=False)
    
