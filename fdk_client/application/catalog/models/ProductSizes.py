"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SizeChart import SizeChart



from .ProductSize import ProductSize







from .ProductSizeStores import ProductSizeStores



from .ProductListingPrice import ProductListingPrice





class ProductSizes(BaseSchema):
    #  swagger.json

    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    sellable = fields.Boolean(required=False)
    
