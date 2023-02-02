"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .ProductVariants import ProductVariants



class ProductVariantsResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    variants = fields.List(fields.Nested(ProductVariants, required=False), required=False)
    
