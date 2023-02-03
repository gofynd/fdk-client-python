"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SEOData import SEOData







from .MOQData import MOQData





class OwnerAppItemResponse(BaseSchema):
    #  swagger.json

    
    seo = fields.Nested(SEOData, required=False)
    
    alt_text = fields.Dict(required=False)
    
    is_cod = fields.Boolean(required=False)
    
    moq = fields.Nested(MOQData, required=False)
    
    is_gift = fields.Boolean(required=False)
    
