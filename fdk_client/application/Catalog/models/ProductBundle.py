"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductGroupingModel import ProductGroupingModel



class ProductBundle(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ProductGroupingModel, required=False), required=False)
    
