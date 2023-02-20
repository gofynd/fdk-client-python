"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductDetailAttribute import ProductDetailAttribute



class ProductDetailGroupedAttribute(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    
