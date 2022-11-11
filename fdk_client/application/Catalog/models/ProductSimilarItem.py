"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductDetail import ProductDetail



class ProductSimilarItem(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
