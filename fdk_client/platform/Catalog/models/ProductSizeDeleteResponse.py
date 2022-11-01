"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ProductSizeDeleteDataResponse import ProductSizeDeleteDataResponse



class ProductSizeDeleteResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ProductSizeDeleteDataResponse, required=False)
    
