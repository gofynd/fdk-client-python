"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductSize import ProductSize



from .SizeChart import SizeChart



from .ProductListingPrice import ProductListingPrice



from .ProductSizeStores import ProductSizeStores





class ProductSizes(BaseSchema):
    #  swagger.json

    
    multi_size = fields.Boolean(required=False)
    
    sellable = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    discount = fields.Str(required=False)
    
