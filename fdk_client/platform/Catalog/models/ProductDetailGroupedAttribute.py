"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ProductDetailAttribute import ProductDetailAttribute



class ProductDetailGroupedAttribute(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    
