"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductSizeStores import ProductSizeStores

from .ProductListingPrice import ProductListingPrice

from .SizeChart import SizeChart

from .ProductSize import ProductSize


class ProductSizes(BaseSchema):
    # Catalog swagger.json

    
    sellable = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    

