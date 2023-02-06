"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductsReasonsFilters1 import ProductsReasonsFilters1

from .ProductsReasonsData1 import ProductsReasonsData1


class ProductsReasons1(BaseSchema):
    # Order swagger.json

    
    filters = fields.List(fields.Nested(ProductsReasonsFilters1, required=False), required=False)
    
    data = fields.Nested(ProductsReasonsData1, required=False)
    

