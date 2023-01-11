"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductBrand import ProductBrand

from .ProductBrand import ProductBrand

from .ProductBrand import ProductBrand


class ProductCategoryMap(BaseSchema):
    # Catalog swagger.json

    
    l3 = fields.Nested(ProductBrand, required=False)
    
    l2 = fields.Nested(ProductBrand, required=False)
    
    l1 = fields.Nested(ProductBrand, required=False)
    

