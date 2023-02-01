"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .ProductVariantItemResponse import ProductVariantItemResponse



class ProductVariantListingResponse(BaseSchema):
    #  swagger.json

    
    total = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductVariantItemResponse, required=False), required=False)
    
