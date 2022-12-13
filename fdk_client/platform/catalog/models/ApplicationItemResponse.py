"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .MOQ import MOQ



from .SEO import SEO



class ApplicationItemResponse(BaseSchema):
    #  swagger.json

    
    alt_text = fields.Dict(required=False)
    
    moq = fields.Nested(MOQ, required=False)
    
    seo = fields.Nested(SEO, required=False)
    
