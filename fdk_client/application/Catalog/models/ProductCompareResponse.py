"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AttributeMetadata import AttributeMetadata





from .ProductDetail import ProductDetail





class ProductCompareResponse(BaseSchema):
    #  swagger.json

    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    
    subtitle = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    title = fields.Str(required=False)
    
