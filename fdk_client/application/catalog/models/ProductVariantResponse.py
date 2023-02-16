"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductVariantItemResponse import ProductVariantItemResponse





class ProductVariantResponse(BaseSchema):
    #  swagger.json

    
    display_type = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductVariantItemResponse, required=False), required=False)
    
    key = fields.Str(required=False)
    
