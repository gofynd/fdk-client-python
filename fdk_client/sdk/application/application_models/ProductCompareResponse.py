"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .ProductDetail import ProductDetail



from .AttributeMetadata import AttributeMetadata


class ProductCompareResponse(BaseSchema):
    # Catalog swagger.json

    
    subtitle = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    title = fields.Str(required=False)
    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    

