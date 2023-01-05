"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductDetail import ProductDetail



from .AttributeMetadata import AttributeMetadata



class ProductsComparisonResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    
