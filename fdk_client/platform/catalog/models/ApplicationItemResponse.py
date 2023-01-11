"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MOQData import MOQData









from .SEOData import SEOData



class ApplicationItemResponse(BaseSchema):
    #  swagger.json

    
    moq = fields.Nested(MOQData, required=False)
    
    alt_text = fields.Dict(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    is_cod = fields.Boolean(required=False)
    
    seo = fields.Nested(SEOData, required=False)
    
