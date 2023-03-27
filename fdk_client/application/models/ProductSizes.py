"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SizeChart import SizeChart



from .ProductListingPrice import ProductListingPrice

from .ProductSizeStores import ProductSizeStores

from .ProductSize import ProductSize




class ProductSizes(BaseSchema):
    # Catalog swagger.json

    
    discount = fields.Str(required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sellable = fields.Boolean(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    

