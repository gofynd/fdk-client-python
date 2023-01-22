"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductSize import ProductSize









from .SizeChart import SizeChart



from .ProductSizeStores import ProductSizeStores



from .ProductListingPrice import ProductListingPrice



class ProductSizes(BaseSchema):
    #  swagger.json

    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    