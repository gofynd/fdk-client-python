"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductSimilarItem import ProductSimilarItem



class SimilarProductByTypeResponse(BaseSchema):
    #  swagger.json

    
    similars = fields.Nested(ProductSimilarItem, required=False)
    
