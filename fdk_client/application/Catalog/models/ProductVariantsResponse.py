"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductVariantResponse import ProductVariantResponse



class ProductVariantsResponse(BaseSchema):
    #  swagger.json

    
    variants = fields.List(fields.Nested(ProductVariantResponse, required=False), required=False)
    
