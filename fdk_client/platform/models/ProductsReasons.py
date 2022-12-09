"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductsReasonsData import ProductsReasonsData

from .ProductsReasonsFilters import ProductsReasonsFilters


class ProductsReasons(BaseSchema):
    # OrderManage swagger.json

    
    data = fields.Nested(ProductsReasonsData, required=False)
    
    filters = fields.List(fields.Nested(ProductsReasonsFilters, required=False), required=False)
    

