"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductListingPrice import ProductListingPrice



from .ProductSize import ProductSize



from .ProductSizeStores import ProductSizeStores





from .SizeChart import SizeChart







class ProductSizes(BaseSchema):
    #  swagger.json

    
    price = fields.Nested(ProductListingPrice, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    multi_size = fields.Boolean(required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sellable = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
