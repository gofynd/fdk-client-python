"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSizeStores import ProductSizeStores







from .ProductSize import ProductSize

from .SizeChart import SizeChart

from .ProductListingPrice import ProductListingPrice


class ProductSizes(BaseSchema):
    # Catalog swagger.json

    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    sellable = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    

