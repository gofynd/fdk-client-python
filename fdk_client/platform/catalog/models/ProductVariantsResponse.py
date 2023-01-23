"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductVariants import ProductVariants



from .Page import Page



class ProductVariantsResponse(BaseSchema):
    #  swagger.json

    
    variants = fields.List(fields.Nested(ProductVariants, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
